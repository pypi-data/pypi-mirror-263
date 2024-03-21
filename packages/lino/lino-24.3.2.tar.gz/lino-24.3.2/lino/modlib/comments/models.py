# -*- coding: UTF-8 -*-
# Copyright 2013-2024 Rumma & Ko Ltd
# License: GNU Affero General Public License v3 (see file COPYING for details)

# from html import escape
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.db import models
from django.db.models import Q
from django.core import validators
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from etgen.html import E, tostring, fromstring

from lino.api import dd, rt, _

from lino.mixins import CreatedModified, BabelNamed
from lino.mixins.periods import DateRangeObservable
from lino.modlib.users.mixins import UserAuthored
from lino.modlib.notify.mixins import ChangeNotifier
from lino.modlib.search.mixins import ElasticSearchable
from lino.modlib.gfks.mixins import Controllable
from lino.modlib.memo.mixins import Previewable, MemoReferrable
from lino.modlib.publisher.mixins import Publishable
from .choicelists import CommentEvents, Emotions
from .mixins import Commentable, MyEmotionField, CommentField
# from .choicelists import PublishAllComments, PublishComment

if dd.is_installed("inbox"):
    from lino_xl.lib.inbox.models import comment_email


class CommentType(BabelNamed):

    class Meta(object):
        abstract = dd.is_abstract_model(__name__, 'CommentType')
        verbose_name = _("Comment Type")
        verbose_name_plural = _("Comment Types")


class Comment(CreatedModified, UserAuthored, Controllable, ElasticSearchable,
              ChangeNotifier, Previewable, Publishable, DateRangeObservable,
              MemoReferrable):

    class Meta(object):
        app_label = 'comments'
        abstract = dd.is_abstract_model(__name__, 'Comment')
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    # elastic search indexes
    ES_indexes = [('comment', {
        "mappings": {
            "properties": {
                "body": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    },
                    "analyzer": "autocomplete",
                    "search_analyzer": "autocomplete_search"
                },
                "body_full_preview": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    },
                    "analyzer": "autocomplete",
                    "search_analyzer": "autocomplete_search"
                },
                "body_short_preview": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    },
                    "analyzer": "autocomplete",
                    "search_analyzer": "autocomplete_search"
                },
                "model": {
                    "type": "text",
                    "fields": {
                        "keyword": {
                            "type": "keyword",
                            "ignore_above": 256
                        }
                    },
                    "analyzer": "autocomplete",
                    "search_analyzer": "autocomplete_search"
                },
                "modified": {
                    "type": "date"
                },
                "owner_id": {
                    "type": "long"
                },
                "owner_type": {
                    "type": "long"
                },
                "private": {
                    "type": "boolean"
                },
                "user": {
                    "type": "long"
                }
            }
        }
    })]

    # publisher_location = "c"
    memo_command = "comment"

    reply_to = dd.ForeignKey('self',
                             blank=True,
                             null=True,
                             verbose_name=_("Reply to"),
                             related_name="replies_to_this")
    # more_text = dd.RichTextField(_("More text"), blank=True)

    private = models.BooleanField(_("Confidential"),
                                  default=dd.plugins.comments.private_default)

    comment_type = dd.ForeignKey('comments.CommentType', blank=True, null=True)
    # reply_vote = models.BooleanField(_("Upvote"), null=True, blank=True)
    # reply_vote = models.SmallIntegerField(_("Vote"), default=0,
    #     validators=[validators.MinValueValidator(-1),
    #         validators.MaxValueValidator(1)])

    my_emotion = MyEmotionField()

    reply = CommentField("comments.RepliesByComment")

    def is_public(self):
        return not self.private

    def disabled_fields(self, ar):
        s = super().disabled_fields(ar)
        if ar.get_user().is_anonymous:
            s.add('my_emotion')
        return s

    def get_my_emotion(self, ar):
        if ar is None:
            return
        u = ar.get_user()
        if u.is_anonymous:
            return
        mr = rt.models.comments.Reaction.objects.filter(user=u,
                                                        comment=self).first()
        if mr:
            return mr.emotion

    def as_story_item(self, ar, indent=0):
        header = ar.obj2htmls(self, self.created_natural)
        header += str(_(" by "))
        header += ar.obj2htmls(self.user)
        # header += ":"
        s = "<h3>{}</h3>".format(header)

        s += self.body_full_preview

        # try:
        #     full_preview_elem = fromstring(self.body_full_preview)
        # except:
        #     full_preview_elem = fromstring("<p>" + self.body_full_preview + "</p>")

        if self.replies_to_this.count():
            # s += "<p>{}</p>".format("Replies:")
            for child in self.replies_to_this.all():
                s += child.as_story_item(ar, indent=indent + 1)
        s += "<br/>"
        style = "margin-left: {}em;".format(indent * 2)
        return '<div style="{}">{}</div>'.format(style, s)

    def __str__(self):
        return '{} #{}'.format(self._meta.verbose_name, self.pk)
        # return _('{user} {time}').format(
        #     user=self.user, obj=self.owner,
        #     time=naturaltime(self.modified))

    # def disabled_fields(self, ar):
    #     rv = super(Comment, self).disabled_fields(ar)
    #     if not self.reply_to_id:
    #         # rv.add("do_pick_reply_emotion")
    #         # rv.add("pick_reply_emotion")
    #         rv.add("reply_emotion")
    #         rv.add("reply_vote")
    #     return rv

    @classmethod
    def get_user_queryset(cls, user):
        qs = super().get_user_queryset(user)

        if not user.user_type.has_required_roles([CommentsReader]):
            return qs.none()

        filters = []
        for m in rt.models_by_base(Commentable):
            flt = m.get_comments_filter(user)
            if flt is not None:
                assert not m._meta.abstract
                ct = rt.models.contenttypes.ContentType.objects.get_for_model(
                    m)
                filters.append(flt | ~Q(owner_type=ct))
        if len(filters):
            qs = qs.filter(*filters)
        return qs.distinct()  # add distinct because filter might be on a join

    # def after_ui_create(self, ar):
    #     super(Comment, self).after_ui_create(ar)
    #     if self.owner_id:
    #         self.private = self.owner.is_comment_private(self, ar)

    def on_create(self, ar):
        super().on_create(ar)
        if self.owner_id:
            self.private = self.owner.is_comment_private(self, ar)

    def after_ui_save(self, ar, cw):
        super().after_ui_save(ar, cw)
        if self.owner_id:
            self.owner.on_commented(self, ar, cw)

    def full_clean(self):
        super().full_clean()
        if self.reply_to_id and not self.owner_id:
            # added only 2023-11-19
            self.owner = self.reply_to.owner
        # self.owner.setup_comment(self)

    def get_change_owner(self):
        return self.owner or self

    # def get_change_message_type(self, ar):
    #     if self.published is None:
    #         return None
    #     return super(Comment, self).get_change_message_type(ar)

    def get_change_observers(self, ar=None):
        if isinstance(self.owner, ChangeNotifier):
            obs = self.owner
        else:
            obs = super()
        for u in obs.get_change_observers(ar):
            yield u

    def get_change_subject(self, ar, cw):
        if cw is None:
            s = _("{user} commented on {obj}")
        else:
            s = _("{user} modified comment on {obj}")
        return s.format(user=ar.get_user(), obj=self.owner)

    def get_change_body(self, ar, cw):
        if cw is None:
            s = _("{user} commented on {obj}")
        else:
            s = _("{user} modified comment on {obj}")
        user = ar.get_user()
        # s = s.format(user=user, obj=self.owner.obj2memo())
        # return ar.obj2htmls(self.owner)
        s = s.format(user=user, obj=ar.obj2htmls(self.owner))
        # s += " (20240101 ar is {})".format(escape(str(ar)))
        if dd.is_installed("inbox"):
            # raise Exception("20230216")
            #mailto:ADDR@HOST.com?subject=SUBJECT&body=Filling%20in%20the%20Body!%0D%0Afoo%0D%0Abar
            s += ' <a href="{href}">{reply}</a>'.format(
                href=comment_email.gen_href(self, user), reply=_("Reply"))

        s += ':<br>' + self.body
        # if False:
        #     s += '\n<p>\n' + self.more_text
        return s

    @classmethod
    def setup_parameters(cls, fields):
        fields.update(observed_event=CommentEvents.field(blank=True))
        super().setup_parameters(fields)

    @classmethod
    def get_request_queryset(cls, ar, **filter):
        qs = super().get_request_queryset(ar, **filter)
        pv = ar.param_values
        if pv.observed_event:
            qs = pv.observed_event.add_filter(qs, pv)
        return qs

    # @dd.htmlbox()
    # def card_summary(self, ar):
    #     if not ar:
    #         return ""
    #     # header = ar.actor.get_comment_header(self, ar) if ar else ""
    #     body = ar.parse_memo(self.body)
    #     # for e in lxml.html.fragments_fromstring(self.body_short_preview):  # , parser=cls.html_parser)
    #     #     html += tostring(e)
    #
    #     return "<div><p>{}</p></div>".format(
    #         # header,
    #         body)

    # def summary_row(o, ar):


dd.update_field(Comment, 'user', editable=False)
Comment.update_controller_field(verbose_name=_('Topic'))
Comment.add_picker('my_emotion')


class Reaction(CreatedModified, UserAuthored, DateRangeObservable):

    class Meta(object):
        app_label = 'comments'
        abstract = dd.is_abstract_model(__name__, 'Reaction')
        verbose_name = _("Reaction")
        verbose_name_plural = _("Reactions")

    allow_cascaded_delete = 'user comment'

    comment = dd.ForeignKey('comments.Comment',
                            related_name="reactions_to_this")
    emotion = Emotions.field(default="ok")


# @dd.receiver(dd.post_startup)
# def setup_memo_commands(sender=None, **kwargs):
#     # See :doc:`/specs/memo`
#
#     if not sender.is_installed('memo'):
#         return
#
#     Comment = sender.models.comments.Comment
#     mp = sender.plugins.memo.parser
#
#     mp.register_django_model('comment', Comment)

from lino.modlib.checkdata.choicelists import Checker


class CommentChecker(Checker):
    # temporary checker to fix #4084 (Comment.owner is empty when replying to a comment)
    verbose_name = _("Check for missing owner in reply to comment")
    model = Comment
    msg_missing = _("Missing owner in reply to comment.")

    def get_checkdata_problems(self, obj, fix=False):
        if obj.reply_to_id and not obj.owner_id and obj.reply_to.owner_id:
            yield (True, self.msg_missing)
            if fix:
                obj.full_clean()
                obj.save()


CommentChecker.activate()

from .ui import *

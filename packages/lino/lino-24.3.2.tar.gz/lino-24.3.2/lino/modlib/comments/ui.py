# -*- coding: UTF-8 -*-
# Copyright 2013-2023 Rumma & Ko Ltd
# License: GNU Affero General Public License v3 (see file COPYING for details)

from django.utils.translation import ngettext
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.contrib.contenttypes.models import ContentType
from django.db import models

from lino.api import dd, rt, gettext, _
from lino.modlib.users.mixins import My
from etgen.html import E, tostring
import lxml
# from lino.utils.soup import truncate_comment
from lino import mixins
from lino.core import constants
from lino.core.utils import qs2summary
from lino.core.gfks import gfk2lookup
from lino.core import constants
from .roles import CommentsReader, CommentsUser, CommentsStaff
from .choicelists import CommentEvents, Emotions
from .mixins import Commentable


class CommentTypes(dd.Table):
    required_roles = dd.login_required(CommentsStaff)
    model = 'comments.CommentType'
    column_names = "name *"
    order_by = ["name"]

    insert_layout = """
    name
    id
    """

    detail_layout = """
    id name
    comments.CommentsByType
    """


class CommentDetail(dd.DetailLayout):
    main = "general more"

    general = dd.Panel("""
    general1:30 general2:30
    """,
                       label=_("General"))

    general1 = """
    owner private
    reply_to pick_my_emotion
    body #body_full_preview
    """
    general2 = """
    reply
    RepliesByComment
    """

    more = dd.Panel("""
    #body more2
    """, label=_("More"))

    more2 = """
    id user
    owner_type owner_id
    created modified
    comment_type
    """


class Comments(dd.Table):
    required_roles = dd.login_required(CommentsUser)

    model = 'comments.Comment'
    params_layout = "start_date end_date observed_event user reply_to"

    insert_layout = dd.InsertLayout(
        """
    reply_to owner owner_type owner_id
    # comment_type
    body
    private
    """,
        window_size=(60, 15),
        hidden_elements="reply_to owner owner_type owner_id")

    detail_layout = "comments.CommentDetail"

    card_layout = dd.Panel("""
    # reply_to owner owner_type owner_id
    # comment_type
    body_short_preview
    # private
    """,
                           label=_("Cards"))

    # html_parser = etree.HTMLParser()

    # ~ column_names = "id date user type event_type subject * body_html"
    # ~ column_names = "id date user event_type type project subject * body"
    # ~ hide_columns = "body"
    # ~ hidden_columns = frozenset(['body'])
    # ~ order_by = ["id"]
    # ~ label = _("Notes")

    @classmethod
    def get_simple_parameters(cls):
        for p in super(Comments, cls).get_simple_parameters():
            yield p
        yield "reply_to"

    @classmethod
    def get_card_title(cls, ar, obj):
        """Overrides the default behaviour
        """
        return cls.get_comment_header(obj, ar)
        # title = _("Created {created} by {user}").format(
        #     created=naturaltime(obj.created), user=str(obj.user))
        # if cls.get_view_permission(ar.get_user().user_type):
        #     title = tostring(ar.obj2html(obj, title))
        # return title

    # @classmethod
    # def get_table_summary(cls, obj, ar):
    #     # print("20190926 get_table_summary", ar.request)
    #     sar = cls.request_from(ar, master_instance=obj, limit=cls.preview_limit)
    #     # print "20170208", sar.limit
    #     # chunks = []
    #     # for o in sar.sliced_data_iterator:
    #     #     chunks.append(E.p(*o.as_summary_row(ar)))
    #     # return E.div(*chunks)
    #     chunks = [o.as_summary_row(ar) for o in sar.sliced_data_iterator]
    #     html = '\n'.join(chunks)
    #     return "<div>{}</div>".format(html)

    @classmethod
    def get_comment_header(cls, comment, ar):
        if (comment.modified - comment.created).total_seconds() < 1:
            t = _("Created " + comment.created.strftime('%Y-%m-%d %H:%M'))
        else:
            t = _("Modified " + comment.modified.strftime('%Y-%m-%d %H:%M'))
        ch = ar.obj2htmls(comment, naturaltime(comment.created), title=t)
        ch += " " + _("by") + " "
        if comment.user is None:
            ch += _("system")
        else:
            ch += ar.obj2htmls(comment.user)

        if cls.insert_action is not None:
            sar = cls.insert_action.request_from(ar)
            # print(20170217, sar)
            sar.known_values = dict(reply_to=comment,
                                    **gfk2lookup(comment.__class__.owner,
                                                 comment.owner))
            # if ar.get_user().is_authenticated:
            if sar.get_permission():
                btn = sar.ar2button(None, _(" Reply "), icon_name=None)
                # btn.set("style", "padding-left:10px")
                ch += " [" + tostring(btn) + "]"

        # ch.append(' ')
        # ch.append(
        #     E.a(u"⁜", onclick="toggle_visibility('comment-{}');".format(
        #         comment.id), title=str(_("Hide")), href="#")
        # )
        return ch

    # @classmethod
    # def as_li(cls, self, ar):
    #     # chunks = [ar.parse_memo(self.body_short_preview)]
    #     chunks = [self.body_short_preview]
    #
    #     by = _("{0} by {1}").format(
    #         naturaltime(self.created), str(self.user))
    #
    #     if (self.modified - self.created).total_seconds() < 1:
    #         t = _("Created " + self.created.strftime('%Y-%m-%d %H:%M') )
    #     else:
    #         t = _("Modified " + self.modified.strftime('%Y-%m-%d %H:%M') )
    #
    #     chunks += [
    #         " (", tostring(ar.obj2html(self, by, title=t)), ")"
    #     ]
    #     # if self.more_text:
    #     #     chunks.append(" (...)")
    #
    #     if ar.get_user().authenticated:
    #         sar = cls.insert_action.request_from(ar)
    #         # print(20170217, sar)
    #         sar.known_values = dict(reply_to=self, owner=self.owner)
    #         if sar.get_permission():
    #             btn = sar.ar2button(
    #                 None, _("Reply"), icon_name=None)
    #             chunks.append(' '+tostring(btn))
    #
    #
    #     html = ''.join(chunks)
    #     return html
    #     # return "<li>" + html + "</li>"


class MyComments(My, Comments):
    required_roles = dd.login_required(CommentsUser)
    auto_fit_column_widths = True
    order_by = ["-modified"]
    column_names = "id modified body_short_preview owner workflow_buttons *"


class AllComments(Comments):
    required_roles = dd.login_required(CommentsStaff)
    order_by = ["-created"]


class CommentsByX(Comments):
    required_roles = dd.login_required(CommentsReader)
    order_by = ["-created"]
    # order_by = ["-modified"]
    # display_mode = ((None, constants.DISPLAY_MODE_SUMMARY), )
    display_mode = ((None, constants.DISPLAY_MODE_LIST), )
    # card_layout = dd.DetailLayout("""
    # card_summary
    # RepliesByComment
    # """)

    @classmethod
    def get_request_queryset(cls, ar, **filter):
        qs = super().get_request_queryset(ar, **filter)
        qs = qs.annotate(num_replies=models.Count('replies_to_this'))
        qs = qs.annotate(num_reactions=models.Count('reactions_to_this'))
        # qs = qs.annotate(my_emotion='reaction__emotion')
        return qs

    @classmethod
    def unused_get_table_summary(cls, obj, ar):
        # sar = cls.request_from(ar, master_instance=obj, is_on_main_actor=False)
        sar = cls.request(parent=ar,
                          master_instance=obj,
                          is_on_main_actor=False)
        elems = ""

        if cls.insert_action is not None:
            if not cls.editable:
                raise Exception("20210515 {}", cls)
            ir = cls.insert_action.request_from(sar)
            if cls is not ir.actor:
                raise Exception("20210515b {}", cls)
            if ir.get_permission():
                if isinstance(obj, cls.model):
                    # we are showing the replies to another comment
                    ir.known_values.update(reply_to=obj)
                    ir.known_values.update(owner=obj.owner)
                    # **gfk2lookup(obj.__class__.owner, obj.owner)
                    ir.clear_cached_status()
                    # btn = ir.ar2button(None, _(" Reply "), icon_name=None)
                    btn = ir.ar2button(None,
                                       title=_("Reply to {} about {}").format(
                                           obj, obj.owner))
                    # btn.set("style", "padding-left:10px")
                    elems += "<p>{}</p>".format(tostring(btn))
                    # elems += [" [", btn, "]"]
                elif isinstance(obj, Commentable):
                    # we are showing the comment about a Commentable
                    btn = ir.ar2button(
                        None,
                        title=_("Start a new {} about {}").format(
                            cls.model._meta.verbose_name, obj))
                    # btn = ir.ar2button(
                    #         None, _("Write new comment:"), # icon_name=None,
                    #         title=_("Start a new comment about {}").format(obj))
                    elems += "<p>{}</p>".format(tostring(btn))
                    # elems += [" [", btn, "]"]
                else:
                    # this should never happen...
                    pass

        n = 0
        for com in sar.data_iterator:
            n += 1
            if n > cls.preview_limit:
                elems += "<p>{}</p>".format("...")
                break
            # elems += "<p>{}</p>".format(cls.as_summary_row(sar, com))
            elems += "<p>{}</p>".format(sar.row_as_paragraph(com))

        return "<div>{}</div>".format(elems)

    @classmethod
    def row_as_paragraph(cls, ar, o, **kw):

        # Here we do another db request on each comment just to get the user's
        # emotion. That's suboptimal and should rather be a annotation:

        s = ""

        if o.num_reactions:
            e = o.get_my_emotion(ar)
            if e is not None:
                s += " {} ".format(e.button_text or e.text)
            # else:
            #     yield " foo "

        # Reaction = rt.models.comments.Reaction
        # qs = Reaction.objects.filter(comment=o)
        # c = qs.count()
        # if c:
        #     my_reaction = qs.filter(user=ar.get_user()).first()
        #     if my_reaction and my_reaction.emotion:

        #
        if o.modified is None or (o.modified - o.created).total_seconds() < 1:
            t = _("Created " + o.created.strftime('%Y-%m-%d %H:%M'))
        else:
            t = _("Modified " + o.modified.strftime('%Y-%m-%d %H:%M'))

        # if o.emotion.button_text:
        #     yield o.emotion.button_text
        #     yield " "

        s += ar.obj2htmls(o, naturaltime(o.created), title=t)
        s += " {} ".format(_("by"))
        if o.user is None:
            by = gettext("system")
        else:
            by = o.user.username
        # yield E.b(by)
        s += "<b>{}</b>".format(by)

        # Show `reply_to` and `owner` unless they are obvious.
        # When `reply_to` is obvious, then `owner` is "obviously obvious" even
        # though that might not be said explicitly.
        if not ar.is_obvious_field('reply_to'):
            if o.reply_to:
                s += " {} ".format(_("in reply to"))
                if o.reply_to.user is None:
                    s += gettext("system")
                else:
                    # yield E.b(o.reply_to.user.username)
                    s += "<b>{}</b>".format(o.reply_to.user.username)
            if not ar.is_obvious_field('owner'):
                if o.owner:
                    s += " {} ".format(_("about"))
                    s += ar.obj2htmls(o.owner)
                    if False:  # tickets show themselves their group in __str__()
                        group = o.owner.get_comment_group()
                        if group and group.ref:
                            s += "@" + group.ref

        if False and o.num_reactions:
            txt = ngettext("{} reaction", "{} reactions",
                           o.num_reactions).format(o.num_reactions)
            s += " ({})".format(txt)

        # replies  = o.__class__.objects.filter(reply_to=o)
        if o.num_replies > 0:
            txt = ngettext("{} reply", "{} replies",
                           o.num_replies).format(o.num_replies)
            s += " ({})".format(txt)

        if o.body_short_preview:
            s += " : " + o.body_short_preview
            # try:
            #     # el = etree.fromstring(o.body_short_preview, parser=html_parser)
            #     for e in lxml.html.fragments_fromstring(o.body_short_preview): #, parser=cls.html_parser)
            #         yield e
            #     # el = etree.fromstring("<div>{}</div>".format(o.body_full_preview), parser=cls.html_parser)
            #     # print(20190926, tostring(el))
            # except Exception as e:
            #     yield "{} [{}]".format(o.body_short_preview, e)
        return s


# class MyPendingComments(MyComments):
#     label = _("My pending comments")
#     welcome_message_when_count = 0

#     @classmethod
#     def param_defaults(cls, ar, **kw):
#         kw = super(MyPendingComments, cls).param_defaults(ar, **kw)
#         kw.update(show_published=dd.YesNo.no)
#         return kw


class RecentComments(CommentsByX):
    # required_roles = dd.login_required(CommentsReader)
    # required_roles = set([CommentsReader])
    allow_create = False
    column_names = "body_short_preview modified user owner *"
    stay_in_grid = True
    # order_by = ["-modified"]
    label = _("Recent comments")
    preview_limit = 10
    # display_mode = ((None, constants.DISPLAY_MODE_SUMMARY), )


class CommentsByType(CommentsByX):
    master_key = 'comment_type'
    column_names = "body created user *"


class CommentsByRFC(CommentsByX):
    master_key = 'owner'
    column_names = "body created user *"
    stay_in_grid = True
    # display_mode = (
    #     (70, constants.DISPLAY_MODE_SUMMARY),
    #     (None, constants.DISPLAY_MODE_STORY),
    # )
    simple_slavegrid_header = True
    insert_layout = dd.InsertLayout("""
    reply_to
    # comment_type
    body
    private
    """,
                                    window_size=(60, 13),
                                    hidden_elements="reply_to")

    @classmethod
    def param_defaults(cls, ar, **kw):
        kw = super().param_defaults(ar, **kw)
        kw['reply_to'] = constants.CHOICES_BLANK_FILTER_VALUE
        return kw

    @classmethod
    def get_main_card(self, ar):
        ticket_obj = ar.master_instance
        if ticket_obj is None:
            return None
        sar = self.request(parent=ar, master_instance=ticket_obj)
        html = ticket_obj.get_rfc_description(ar)
        sar = self.insert_action.request_from(sar)
        if sar.get_permission():
            btn = sar.ar2button(None, _("Write comment"), icon_name=None)
            html += "<p>" + tostring(btn) + "</p>"

        if html:
            return dict(
                card_title="Description",
                main_card_body=html,  # main_card_body is special keyword
                id="[main_card]"  # needed for map key in react...
            )
        else:
            return None

    # @classmethod
    # def get_table_summary(self, obj, ar):
    #     sar = self.request_from(ar, master_instance=obj)
    #     html = obj.get_rfc_description(ar)
    #     sar = self.insert_action.request_from(sar)
    #     if sar.get_permission():
    #         btn = sar.ar2button(None, _("Write comment"), icon_name=None)
    #         html += "<p>" + tostring(btn) + "</p>"
    #
    #     html += "<ul>"
    #     for c in sar:
    #         html += "<li>{}<div id=\"{}\">{}</div></li>".format(
    #             self.get_comment_header(c, sar),
    #             "comment-" + str(c.id),
    #             ar.parse_memo(c.body))
    #
    #     html += "</ul>"
    #     return ar.html_text(html)


class CommentsByMentioned(CommentsByX):
    # show all comments that mention the master instance
    master = dd.Model
    label = _("Mentioned in")
    # label = _("Comments mentioning this")
    # insert_layout = None
    # detail_layout = None
    editable = False

    @classmethod
    def get_filter_kw(cls, ar, **kw):
        mi = ar.master_instance
        if mi is None:
            return None
        Mention = rt.models.memo.Mention
        assert not cls.model._meta.abstract
        ct = ContentType.objects.get_for_model(cls.model)
        mkw = gfk2lookup(Mention.source, mi, owner_type=ct)
        mentions = Mention.objects.filter(**mkw).values_list('owner_id',
                                                             flat=True)
        # mentions = [o.comment_id for o in Mention.objects.filter(**mkw)]
        # print(mkw, mentions)
        # return super(CommentsByMentioned, cls).get_filter_kw(ar, **kw)
        kw.update(id__in=mentions)
        return kw


class RepliesByComment(CommentsByX):
    master_key = 'reply_to'
    stay_in_grid = True
    # display_mode = ((None, constants.DISPLAY_MODE_STORY), )
    # title = _("Replies")
    label = _("Replies")
    simple_slavegrid_header = True

    paginator_template = "PrevPageLink NextPageLink"
    hide_if_empty = True


def comments_by_owner(obj):
    return CommentsByRFC.request(master_instance=obj)


class Reactions(dd.Table):
    required_roles = dd.login_required(CommentsStaff)
    editable = False
    model = "comments.Reaction"
    column_names = "comment user emotion created *"


from lino_xl.lib.pages.choicelists import PageFillers

PageFillers.add_item(RecentComments)

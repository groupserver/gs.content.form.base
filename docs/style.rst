Form style guide
================

Almost all pages in GroupServer_ are forms, and almost all forms
conform to the following `basic style`_ and use the same
terms_. The `GNOME Human Interface Guidelines`_ provided much of
the inspiration for this guide.

Basic style
-----------

Having a consistent style makes a system easier to use. Because
of this link_ to the page, its title_, the introduction_ and the
button_ used to submit the form all use similar phrasing. The
widget fields_ sit between the introduction and the
button. Finally, a `feedback message`_ is displayed.

Link
~~~~

A link to a form is always an imperative verb-phrase:

* Start a group
* Change the privacy
* Set a new password

The verb :term:`change` is always preferred to :term:`edit`.

Title
~~~~~

The main page heading is always an ``<h1>`` element containing
the same verb phrase as the link_, while the ``<title>`` element
contains the site name, group name, or profile name as
appropriate.

==================  ===============================================
Heading             Title
==================  ===============================================
Start a group       Start a group: Example site
Change the privacy  Change the privacy: Initial group: Example site
Set a new password  Set a new password: Administrator: Example site
==================  ===============================================

Initial caps, rather than title case, is used.

Introduction
~~~~~~~~~~~~

If the form has an introductory paragraph it should open with the
verb in the infinitive form:

* To start a group…
* To change the privacy…
* To set your new password…

When possible, *your* is used in the introduction to convey a
sense of inclusion, ownership, and responsibility.


.. note:: This use of *your* does lead to ambiguity about the
          **ownership of a group,** which is owned both by the
          :term:`administrator` and each :term:`member`. In some
          cases there is an over-arching concept of an *owner*
          (such as a corporate body) that is not reflected in
          this use of *your*.

Fields
~~~~~~

A *noun* is used for the ``title`` of each field.

* Group type
* Privacy
* Password

.. note:: The fields are defined using :ref:`the API, <widgets>`
          and are displayed in a consistent manner by the
          :ref:`widgetscp` content provider.

Button
~~~~~~

The button to submit the form always uses the verb from the link_
and title_:

* Start
* Change
* Set

Feedback message
~~~~~~~~~~~~~~~~

When a form has been processed a feedback message is displayed
(by the :ref:`statusMessageCP` content provider). The exception
is when the form *creates* something, when the created object
should be shown.

The feedback message is a complete sentence that refers to the
verb from the link_ in the past-tense, and clarifies what has
been changed (usually linking to the object).

* You have changed the privacy for the *Initial group* to secret.
* You have set your password.

Terms
-----

A consistent set of terms is used to describe the actions_
(verbs) that are carried out on objects_ (nouns).

Actions
~~~~~~~

Some actions are :ref:`general <general>`, while many more are
`specific GroupServer actions`_.

.. _general:

General actions
```````````````

Most forms will just need to use :term:`change` as their sole
action.

.. glossary::
   :sorted:

   Change
     Alter a group, profile, or site (see also :term:`edit`):

       Change the site About box.

   Click
     Buttons and links are clicked.

     * A button_ is explicitly stated as such (use "click" rather
       than "click on"):

         Edit the Message and click the *Change* button.

     * For a link just link-phrase is used:

         To find more details click *view more* below.

   Edit
     Alter a field (see also :term:`change`):

       Edit the Message and click the *Change* button.

   Select
     Check-boxes and radio buttons are selected:

       Select the privacy level from the Privacy list below…

   Visit
     A :term:`person` visits a page:

       Visit the group page to see the current activity.

Specific GroupServer actions
````````````````````````````

The following actions have specific meanings in GroupServer.

.. glossary::
   :sorted:

   Add
     An :term:`administrator` will add a :term:`person` to a
     group, after which they become a :term:`group member`.

   Accept
     A :term:`person` will accept an invitation to join a group,
     or a :term:`administrator` will accept a request to become a
     member. See also :term:`decline`.

   Decline
     An invitation to become a :term:`group member` issued by a
     :term:`administrator` may be declined by a
     :term:`person`. Conversely, a person can request to become a
     member, which can be declined by an administrator. See also
     :term:`accept`.

   Invite
     A :term:`person` can be invited to join a group by an
     :term:`administrator`. See also :term:`add`. This is the
     inverse of :term:`request`.

   Leave
     A :term:`person` will leave a :term:`group` when they no
     longer wish to be a :term:`member`. See also
     :term:`unsubscribe`.

   Manage
     Alter the privileges and membership of a :term:`group
     member`:

       Manage the members of GroupServer Development.

   Remove
      A :term:`administrator` may remove a :term:`member` from a
      group. Only members are ever removed, use the term
      :term:`revoke` for privileges. See also :term:`leave`.

   Request
     If a :term:`person` wishes to join a private group then they
     can request membership of the group.

   Revoke
     Privileges are *revoked* from a :term:`member` to prevent
     the action from being confused with :term:`remove`:

        You have revoked group administrator privileges from
        *Example member*. They are now a normal member of this
        group.

   Unsubscribe
      A particular way to leave a group by sending a message to
      the group with ``Unsubscribe`` as the
      :mailheader:`Subject`. Prefer the term :term:`leave` in the
      general case.

Objects
~~~~~~~

There are three main actors in GroupServer: a :term:`profile`, a
:term:`group`, and a :term:`site`.

.. glossary::
   :sorted:

   Address
   Email address
     Use *address* rather than *email address*, unless there is
     possible ambiguity with a *Web page address* (also known as
     a URL). The term *email* could mean an address, or a
     :term:`message` and should be avoided. Each :term:`group`
     has a single address, while a :term:`person` can have
     multiple addresses associated with their :term:`profile`.

   Administrator
   Group administrator
   Site administrator
     A person that can alter a :term:`group` or :term:`site`, as
     opposed to a :term:`normal member`.

   Archive
     The topics and posts in a :term:`group` are known as the
     archive (see also :term:`post`, and :term:`topic`):

       The group page shows the archive of posts that have been
       added.

   Attachment
     An attachment is only used in when discussing an
     :term:`email message`: they are stripped when the processed
     by them :term:`group` and replaced with a link, which is
     then referred to as a :term:`file`.

   File
     A file is *associated* with a :term:`post`. It appears in a
     list in the bottom of the post, both in the :term:`archive`
     and in the :term:`email message` sent from the group.

   Group
     In GroupServer a group is analogous to a *listserv* or
     *forum* in other systems. A :term:`person` is a
     :term:`member` of a group, and the group belongs to a
     :term:`site`. Each group has an :term:`email address` that
     people can use to make a :term:`post`, which is shown in the
     :term:`archive` found on the :term:`group page`.

   Group page
     The web page for a :term:`group`, as opposed to the
     :term:`homepage`:

        Visit the group page at
        <http://groupserver.org/groups/development>.

   Homepage
     The web page for a :term:`site` rather than the :term:`group
     page`:

       Visit the homepage at <http://groupserver.org/>.

   Member
   Group member
   Site member
     A :term:`person` that belongs to a site or group (explicitly
     or implicitly):

       You are a member of GroupServer Development.

   Message
   Email message
     A message is either

     * Sent to a :term:`group` when someone makes a :term:`post`
       using email, or
     * Sent from the group after someone has made a post.

     It can be referred to as a *message* if there is no
     ambiguity with the `feedback message`_; the term *email* is
     easily confused with an :term:`address` and should be
     avoided. See also :term:`notification`.

   Normal member
     A **normal** member is a group member that lacks
     :term:`administrator` privileges. In a **discussion** group
     a normal member can add and view a :term:`post`, while in an
     **announcement** group a normal member can only view posts
     (see :term:`posting member`).

   Notification
      An :term:`email message` sent by GroupServer for any reason
      *other* than a :term:`person` making a :term:`post`:

        Because you are a :term:`group administrator` you will
        receive a notification whenever someone leaves your
        :term:`group`.

   Posting member
     A member of an **announcement** group that can add posts to
     the group.

   Person
   User
     Avoid the term *user*, preferring *person* at the very
     least. However, :term:`member` or :term:`administrator`
     should be used in preference to either. In all cases *they*
     is used as a gender-neutral singular.

   Post
     A post is made to a :term:`group` by a :term:`member`, and
     organised into a :term:`topic`. It may be posted using the
     web interface to GroupServer, or by sending an :term:`email
     message` to the group. It may be associated with a
     :term:`file`.

   Profile
     The data associated with a person. Try and distinguish
     between the profile and the :term:`person`:

       To add an email address to your profile….

   Site
     Each :term:`group` belongs to a site, and a :term:`profile`
     is shared between the different groups.  A GroupServer site
     sits at the top of a domain; the index-page for this domain
     is referred to as the :term:`homepage`.

   Topic
     One or more posts with the same :mailheader:`Subject` are
     organised into a topic within a :term:`group`. See also
     :term:`post`.

.. _GroupServer: http://groupserver.org/
.. _GNOME Human Interface Guidelines:
   https://developer.gnome.org/hig/stable/

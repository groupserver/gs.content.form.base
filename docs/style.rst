Form style guide
================

All forms in GroupServer conform to the following style.

Basic style
-----------

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
* To set a new password…

Button
~~~~~~

The button to submit the form always uses the verb from the link_
and title_:

* Start
* Change
* Set

Glossary
--------

Actions_ (verbs) are carried out on objects_ (nouns).

Actions
~~~~~~~

When in doubt, use :term:`change`.

.. glossary::

   Add
     A :term:`person` can be added to a group, after which they
     become a :term:`group member`.

   Accept
     A :term:`person` may accept an invitation to join a group,
     or a :term:`administrator` can accept the request to become
     a member. See also :term:`decline`.

   Change
     Alter a group, profile, or site: *Change the site About
     box*. See also :term:`Edit`.

   Click
     If a person clicks a button_ then it is explicitly stated
     that it is a button: *Click the Change button*. (Only
     *click* rather than *click on*.)  If a person uses a link
     then just the link-phrase is used: *To find more details
     click "view more"*.

   Decline
     An invitation to become a :term:`group member` issued by a
     :term:`administrator` may be declined by a
     :term:`person`. Conversely, a person can request to become a
     member, which can be declined by an administrator.

   Edit
     Alter a field: *Edit the Message and click Change.* See
     also :term:`Change`.

   Invite
     A :term:`person` can be invited to join a group by an
     :term:`administrator`. See also :term:`add`. This is the
     inverse of :term:`request`.

   Request
     If a :term:`person` wishes to join a private group then they
     can request membership of the group.

   Select
     Check-boxes and radio buttons are selected: *Select
     the privacy level from the Privacy list below…*

   Visit
     A :term:`person` visits a page: *Visit the group page to see
     the current activity*.

Objects
~~~~~~~

There are three main actors in GroupServer: a :term:`profile`, a
:term:`group`, and a :term:`site`.

.. glossary::

   Address
   Email address
     Use *Email address* to avoid ambiguity with a *web page
     address* (also known as a URL). The term *email* could mean
     an address, or a :term:`post`. Each :term:`group` has a
     single address, while a :term:`person` can have multiple
     addresses associated with their :term:`profile`.

   Administrator
   Group administrator
   Site administrator
     A person that can alter a site or group, as opposed to a
     :term:`normal member`.

   File
   Attachment
     A file is *associated* with a :term:`post`. An attachment is
     only used with an :term:`email message`: they are stripped
     when the processed by them :term:`group` and replaced with a
     link.

   Group
     Analogous to a *listserv* or *forum* in other systems. A
     :term:`person` is a :term:`member` of a group, and the group
     belongs to a :term:`site`. Each group has an email address
     that people can use to make a :term:`post`.

   Member
   Normal member
   Group member
   Site member
     A :term:`person` that belongs to a site or group (explicitly
     or implicitly). A **normal** member is a group member that
     lacks :term:`administrator` privileges.
     
   Person
   User
     Avoid the term *user*, preferring *person* at the very
     least. However, :term:`member` or :term:`administrator`
     should be used in preference to either. In all cases *they*
     is used as a gender-neutral singular.

   Post
   Email message
     A post is made to a :term:`group` by a :term:`member`, and
     organised into a :term:`topic`. It may be posted using the
     web interface to GroupServer, or an email message is sent to
     the address of a group. It may be associated with a
     :term:`file`.

   Profile
     The data associated with a person. Try and distinguish
     between the profile and the :term:`person`: *To add an email
     address to your profile…*.

   Site
     A GroupServer site sits at the top of a domain, such as
     <http://groupserver.org/>. Each :term:`group` belongs to a
     site, and a :term:`profile` is shared between the different
     groups.

   Topic
     One or more posts with the same :mailheader:`Subject` are
     organised into a topic within a :term:`group`. See also
     :term:`post`.

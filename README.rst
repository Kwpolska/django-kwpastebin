=====================
KwPastebin for Django
=====================

A simple, yet stylish, pastebin.

Live: https://go.chriswarrick.com/paste/

License: 3-clause BSD.

Configuration
-------------

Only one option, ``KWPASTEBIN_ANONYMOUS_CAN_ADD`` (defaults to ``False`` —
dangerous!) You’ll also need ``HASHID_FIELD_SALT`` for Hashids.

Run the included ``generate_css.py`` file if you want to generate a different
color scheme (default is ``monokai``).

Caching
-------

Every paste is rendered (through Pygments) when it’s saved. People with the
appropriate permission can invalidate the cache — all pastes will be
re-rendered when they’re first loaded.

Permission model
----------------

* ``kwpastebin.add_paste`` — enables adding pastes on the index page. Overridden by ``KWPASTEBIN_ANONYMOUS_CAN_ADD``.
* ``kwpastebin.modify_paste`` — enables editing of **all** pastes.
* ``kwpastebin.delete_paste`` — enables deletion of **all** pastes.
* ``kwpastebin.modify_own_paste`` — enables editing of pastes created by the current user.
* ``kwpastebin.delete_own_paste`` — enables deletion of pastes created by the current user.
* ``kwpastebin.list_all_pastes`` — enables listing of all pastes. (Every user can get a list of their own pastes.)
* ``kwpastebin.invalidate_cache`` — enables invalidating paste cache. (Admin feature.)

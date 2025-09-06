import litestar

# FIXME: https://api.holoplus.com/v4/talent-channel/channels
# FIXME: https://api.holoplus.com/v4/threads/updated?channel_id=2f495a98-f005-4ef4-b164-be922b823b42&fav_talent_filter=false&filter_language=en&limit=20&offset=
# FIXME: https://api.holoplus.com/v4/threads/e1272fb1-38bc-4e29-aeb8-f8a9443c3340/contents
# FIXME: https://api.holoplus.com/v4/threads/modules?module_id=b91175fc-8190-4dde-8e92-01d58ed48f46&fav_talent_filter=false&filter_language=en&limit=5
# FIXME: https://api.holoplus.com/v4/pins/2f495a98-f005-4ef4-b164-be922b823b42?filter_language=en
# FIXME: https://api.holoplus.com/v4/comments/me?limit=20
# FIXME: https://api.holoplus.com/v4/threads/favorite?limit=20
# FIXME: https://api.holoplus.com/v4/threads/me?limit=20
# FIXME: https://api.holoplus.com/v4/comments/cfdd2f8b-ee45-4e3f-b4df-c150f826e224/contents
# FIXME: https://api.holoplus.com/v4/stream_events?fav_talent_filter=false&plan=past
# FIXME: https://api.holoplus.com/v4/stream_events?fav_talent_filter=false&plan=current
# FIXME: https://api.holoplus.com/v4/stream_events?fav_talent_filter=false&plan=future
# FIXME: https://api.holoplus.com/v4/stream_events/7tyO2iBAdAA
# FIXME: https://api.holoplus.com/v4/talent-channel/channels
# FIXME: https://api.holoplus.com/v4/talent-channel/threads/newest?channel_id=7f237193-e0f7-4127-af78-9f5c255069ac&limit=20
# FIXME: https://api.holoplus.com/v4/talent-channel/comments/popular?thread_id=c7186c9b-6c6d-4269-b4cf-5a2bb97acbd2&limit=20
# FIXME: https://api.holoplus.com/v4/talent-channel/comments/newest?thread_id=c7186c9b-6c6d-4269-b4cf-5a2bb97acbd2&limit=20
# FIXME: https://api.holoplus.com/v4/comments/popular?thread_id=a4d526d1-2c97-476f-ae12-849fdef41eb8&limit=20&filter_language=en
# FIXME: https://api.holoplus.com/v4/comments/e0e5e278-bce6-4baf-b4c1-75272d524749/contents
# FIXME: https://api.holoplus.com/v4/channels/18eec09c-ce17-4f50-bfc6-8b47457882ed/updated_thread?filter_language=en
# FIXME: https://api.holoplus.com/v4/threads/updated?channel_id=69efbc03-aec9-4e33-a6bd-280c36925c00&fav_talent_filter=false&filter_language=en&limit=20&offset=0
# FIXME: POST https://api.holoplus.com/v4/reactions/contents/b2ee47b9-2225-4c25-990a-3c6430531c8e
# FIXME: POST https://api.holoplus.com/v4/threads/c7186c9b-6c6d-4269-b4cf-5a2bb97acbd2/favorite
# FIXME: DELETE https://api.holoplus.com/v4/threads/c7186c9b-6c6d-4269-b4cf-5a2bb97acbd2/favorite

ROUTES: list[litestar.handlers.HTTPRouteHandler] = []

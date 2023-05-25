import json

def getUserMetaInfo(profile):
    return {
            'fullName': profile.full_name,
            'userId': profile.userid,
            'userName': profile.username,
            'bio': profile.biography,
            'bioUrl': profile.external_url,
            'follwersCount': profile.followers,
            'followingCount': profile.followees,
            'postCount': profile.mediacount,
            'igTvCount': profile.igtvcount,
            'isPrivateAccount': profile.is_private,
            'isBusinessAccount' : profile.is_business_account,
            'isVerifiedAccount': profile.is_verified,
            'profilePicUrl': profile.profile_pic_url,
            'businessCategoryName': profile.business_category_name,
            'hasPublicStory': profile.has_public_story,
            }
    

def getPostInfo(post):
    return {
                'mediaId': post.mediaid,
                'isPinned' : post.is_pinned,
                'isVideo': post.is_video,
                'isSponsored':post.is_sponsored,
                'likes':post.likes,
                'location':post.location,
                'mediaCount':post.mediacount,
                'ownerId':post.owner_id,
                'ownerUsername': post.owner_username,
                'taggedUsers': post.tagged_users,
                'videoViewCount':post.video_view_count,
                'postType':post.typename,
                'title': post.title,
                'url': post.url,
                'videoUrl': post.video_url,
                'caption' : post.caption,
                'captionHashtags': post.caption_hashtags,
                'captionMentions': post.caption_mentions,
                'createdDate': post.date_utc,
                'videoDuration': post.video_duration,
            }
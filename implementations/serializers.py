from rest_framework import serializers

from tags.serializers import TagSerializer

from .models import Implementation, ImplementationComment


class ImplementationSerializer(serializers.ModelSerializer):
    owner_avatar = serializers.CharField(source="owner.avatar", read_only=True)
    owner_username = serializers.CharField(source="owner.username", read_only=True)
    bookmarked = serializers.SerializerMethodField(read_only=True)
    viewed = serializers.SerializerMethodField(read_only=True)
    view_count = serializers.IntegerField(read_only=True)
    vote = serializers.SerializerMethodField(read_only=True)
    upvote_count = serializers.IntegerField(read_only=True)
    downvote_count = serializers.IntegerField(read_only=True)
    downvote_count = serializers.IntegerField(read_only=True)
    comments_count = serializers.IntegerField(read_only=True)
    milestones = serializers.ListField(source="idea.milestones", read_only=True)

    def get_bookmarked(self, obj):
        request = self.context.get("request")
        if request is not None:
            return obj.bookmarked_by.filter(pk=request.user.pk).exists()
        return False

    def get_viewed(self, obj):
        request = self.context.get("request")
        if request is not None:
            return obj.views.filter(pk=request.user.pk).exists()
        return False

    def get_vote(self, obj):
        request = self.context.get("request")
        if request is not None:
            if obj.upvotes.filter(pk=request.user.pk).exists():
                return 1
            elif obj.downvotes.filter(pk=request.user.pk).exists():
                return -1
        return 0

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["tags"] = TagSerializer(instance.tags.all(), many=True).data
        return ret

    class Meta:
        model = Implementation
        fields = (
            "id",
            "owner",
            "owner_avatar",
            "owner_username",
            "idea",
            "title",
            "description",
            "body",
            "tags",
            "milestones",
            "completed_milestones",
            "draft",
            "is_validated",
            "is_accepted",
            "bookmarked",
            "viewed",
            "view_count",
            "vote",
            "upvote_count",
            "downvote_count",
            "comments_count",
            "created_at",
            "updated_at",
        )


class ImplementationCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImplementationComment
        fields = "__all__"

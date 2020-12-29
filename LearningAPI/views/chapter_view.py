from django.db.models import Count
from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from LearningAPI.models import Chapter, Book, Project


class ChapterViewSet(ViewSet):
    """Chapter view set"""

    permission_classes = (IsAdminUser,)

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized instance
        """
        chapter = Chapter()
        chapter.name = request.data["name"]

        book = Book.objects.get(pk=int(request.data["course_id"]))
        chapter.book = book

        project = Project.objects.get(pk=int(request.data["project_id"]))
        chapter.project = project

        try:
            chapter.save()
            serializer = ChapterSerializer(Chapter, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response({"reason": ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single item

        Returns:
            Response -- JSON serialized instance
        """
        try:
            Chapter = Chapter.objects.get(pk=pk)

            serializer = ChapterSerializer(Chapter, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests

        Returns:
            Response -- Empty body with 204 status code
        """
        try:
            Chapter = Chapter.objects.get(pk=pk)
            Chapter.name = request.data["name"]

            course = Course.objects.get(pk=int(request.data["course_id"]))
            Chapter.course = course

            Chapter.save()
        except Chapter.DoesNotExist:
            return Response(None, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return HttpResponseServerError(ex)

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single item

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            Chapter = Chapter.objects.get(pk=pk)
            Chapter.delete()

            return Response(None, status=status.HTTP_204_NO_CONTENT)

        except Chapter.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests for all items

        Returns:
            Response -- JSON serialized array
        """
        try:
            Chapters = Chapter.objects.all().order_by('pk')

            serializer = ChapterSerializer(
                Chapters, many=True, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)


class ChapterSerializer(serializers.ModelSerializer):
    """JSON serializer"""

    class Meta:
        model = Chapter
        fields = ('id', 'name',)

class ChapterSerializer(serializers.ModelSerializer):
    """JSON serializer"""
    chapters = ChapterSerializer(many=True)

    class Meta:
        model = Chapter
        fields = ('id', 'name', 'chapters',)
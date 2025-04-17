from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import QueryLog
from .serializers import QueryLogSerializer
from .action_logic import analyze_message, suggest_actions

class AnalyzeView(APIView):
    def post(self, request):
        query = request.data.get("query")
        if not query:
            return Response({"error": "Query field is required"}, status=400)

        analysis = analyze_message(query)
        suggestions = suggest_actions(analysis["tone"], analysis["intent"])

        log = QueryLog.objects.create(
            query=query,
            tone=analysis["tone"],
            intent=analysis["intent"],
            suggested_actions=suggestions
        )

        serializer = QueryLogSerializer(log)
        return Response(serializer.data, status=status.HTTP_200_OK)

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Page, Project
from .serializers import PageSerializer, ProjectSerializer
from rest_framework.permissions import AllowAny
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
from django.template import Context

class ListPages(ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class ListProjects(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class SendEmail(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            subject = request.data.get("subject", "")
            from_email = request.data.get("email", "")
            message = request.data.get("msg", "")
            phone_number = request.data.get("phoneNum", "")
            full_name = request.data.get("fullName", "")
            to = "admin@alsdi.com"

            # Validate coming data.
            if len(subject) > 0 and \
                len(from_email) > 0 and \
                len(message) > 0 and \
                len(phone_number) > 0 and \
                phone_number.isdigit():

                try:
                    # Send data to email template and get email template.
                    html_email_template = get_template("email_template.html").render(
                    {
                        "from": from_email,
                        "subject": subject,
                        "message": message,
                        "phone_num": phone_number,
                        "full_name": full_name
                    }
                    )
                    msg = EmailMultiAlternatives(f"{subject} - رسالة من زوار الموقع", "nothing", from_email, [to])
                    msg.attach_alternative(html_email_template, "text/html")
                    msg.send()
                    return Response({"detail": "Your message was sent"}, status=status.HTTP_200_OK)

                except BadHeaderError:
                    return Response({"detail": "Invalid header found."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"detail": "Data is invalid"}, status=status.HTTP_400_BAD_REQUEST)
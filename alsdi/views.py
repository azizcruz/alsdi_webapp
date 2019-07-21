from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Page, Project, Article
from .serializers import PageSerializer, ProjectSerializer, ArticleSeriaizer
from rest_framework.permissions import AllowAny
from django.core.mail import EmailMultiAlternatives, BadHeaderError, EmailMessage
from django.template.loader import get_template

class ListPages(ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class ListProjects(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ListArticles(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSeriaizer

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


class BookingView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        allowed_types = ['jpg', 'jpeg', 'pdf', 'png', 'html', 'htm']
        data = request.data
        # Get data from body
        email = data.get('email')
        msg = data.get('msg', None)
        full_name = data.get('fullName')
        phone_num = data.get('phoneNum')
        project_subject = data.get('subject')
        project_quoutation = data.get('quoutRange')
        project_type = data.get('projectType')
        level = data.get('level', None)
        file1 = data.get('file1')
        file2 = data.get('file2')
        file3 = data.get('file3')
        file4 = data.get('file4')
        file5 = data.get('file5')

        # Check file type.
        if (
            file1.name.split('.')[1] not in allowed_types or
            file2.name.split('.')[1] not in allowed_types or
            file3.name.split('.')[1] not in allowed_types or
            file4.name.split('.')[1] not in allowed_types or
            file5.name.split('.')[1] not in allowed_types
        ):
            return Response({"detail": "file is not allowed."}, status=status.HTTP_406_NOT_ACCEPTABLE)

        # Check file size.
        if (
            round(file1.size / (1024 * 1024), 3) > 10 or
            round(file2.size / (1024 * 1024), 3) > 10 or
            round(file3.size / (1024 * 1024), 3) > 10 or
            round(file4.size / (1024 * 1024), 3) > 10 or
            round(file5.size / (1024 * 1024), 3) > 10
        ):
            return Response({"detail": "file is greater than 10 mb."}, status=status.HTTP_406_NOT_ACCEPTABLE)

        if (len(email) > 0 and
                len(full_name) > 0 and
                len(phone_num) > 0 and
                len(project_subject) > 0 and
                len(project_type) > 0 and
                len(project_quoutation) > 0 and
                len(level) > 0 and
                file1 and
                file2 and
                file3 and
                file4 and
                file5):



            try:
                body = get_template("email_with_files_template.html").render({
                    "email": email,
                    "msg": msg,
                    "phone_num": phone_num,
                    "full_name": full_name,
                    "project_quoutation": project_quoutation,
                    "project_subject": project_subject,
                    "project_type": project_type,
                    "level": level,
                })
                to = "admin@alsdi.com"
                msg = EmailMessage(f"{full_name} - رسالة حجز موعد من ", body, email, [to])
                msg.attach(filename=file1.name, content=file1.read(), mimetype=file1.content_type)
                msg.attach(filename=file2.name, content=file2.read(), mimetype=file2.content_type)
                msg.attach(filename=file3.name, content=file3.read(), mimetype=file3.content_type)
                msg.attach(filename=file4.name, content=file4.read(), mimetype=file4.content_type)
                msg.attach(filename=file5.name, content=file5.read(), mimetype=file5.content_type)
                msg.content_subtype = "html"
                msg.send()

                return Response({"detail": "Your booking was sent"}, status=status.HTTP_200_OK)

            except BadHeaderError:
                return Response({"detail": "Invalid header found."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "Data is invalid"}, status=status.HTTP_400_BAD_REQUEST)

from django.core.mail import send_mail
from django.conf import settings

from rest_framework import viewsets, status
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from .models import QuickSend, QuickQuote
from .serializers import QuickSendSerializer, QuickQuoteSerializer


class SafeAPIMixin(object):
    """
    Resuable mixin for ModelViewSet to prevent update/list/view.
    """
    def list(self, request, *args, **kwargs):
        return Response({'status': 'Nice Try!'})

    def retrieve(self, request, pk=None, *args, **kwargs):
        return Response({'status': 'Nice Try!'})

    def update(self, request, pk=None, *args, **kwargs):
        return Response({'status': 'Nice Try!'})

    def partial_update(self, request, pk=None, *args, **kwargs):
        return Response({'status': 'Nice Try!'})

    def destroy(self, request, pk=None, *args, **kwargs):
        return Response({'status': 'Nice Try!'})


class QuickSendViewSet(SafeAPIMixin, viewsets.ModelViewSet):
    queryset = QuickSend.objects.all()
    serializer_class = QuickSendSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            customer_name = serializer.validated_data.get('name')
            customer_email = serializer.validated_data.get('email')
            reason = serializer.validated_data.get('reason')
            quicksend = QuickSend(reason=reason)
            reason = quicksend.get_reason_display()

            line_break_txt = "\n\n"
            line_break_html = "<br><br>"
            msg_txt = """
                    New inquiry from *{0}* about \"{1}.\" {3}
                    Client Email: {2}.{3}
                    """.format(customer_name, reason, customer_email,
                    line_break_txt)

            msg_html = """
                    New inquiry from <strong>{0}</strong> about \"{1}.\" {3}
                    Client Email: <a href=\"mailto:{2}\">{2}</a>.{3}
                    """.format(customer_name, reason, customer_email,
                    line_break_html)

            send_mail(subject="Quick Form Inquiry", message=msg_txt,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['joshua@nostalg.io'], fail_silently=True,
                    html_message=msg_html)

        return super(QuickSendViewSet, self).create(request, *args, **kwargs)


class QuickQuoteViewSet(SafeAPIMixin, viewsets.ModelViewSet):
    """
    Inherit the API safety routes.
    """
    queryset = QuickQuote.objects.all()
    serializer_class = QuickQuoteSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            customer_name = serializer.validated_data.get('name')
            customer_email = serializer.validated_data.get('email')
            customer_phone = serializer.validated_data.get('phone')
            project = serializer.validated_data.get('project')

            line_break_txt = "\n\n"
            line_break_html = "<br><br>"
            msg_txt = """
                    New Quote Request from *{0}*.{4}
                    Client Email: {1}.{4}
                    Client Phone: {2}.{4}
                    Project:{4}
                    {3}{4}
                    """.format(customer_name, customer_email, customer_phone,
                        project, line_break_txt)

            msg_html = """
                    New Quote Request from <strong>{0}</strong>.{4}
                    Client Email: <a href=\"mailto:{1}\">{1}</a>.{4}
                    Client Phone: {2}.{4}
                    Project:{4}
                    {3}{4}
                    """.format(customer_name, customer_email, customer_phone,
                        project, line_break_html)

            send_mail(subject="Quote Inquiry", message=msg_txt,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['joshua@nostalg.io'], fail_silently=True,
                    html_message=msg_html)

        return super(QuickQuoteViewSet, self).create(request, *args, **kwargs)

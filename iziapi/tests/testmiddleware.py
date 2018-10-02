from django.core.exceptions import PermissionDenied
from django.urls import reverse
from django.test import RequestFactory, TestCase

from iziapi.middleware import ApiGatewayMiddleWare, parse_session_id
from iziapi.models import ApiKey


class DummyRequest:
    META = {'HTTP_SESSION_ID': None}


class ApiGatewayMiddleWareTest(TestCase):

    rf = RequestFactory()

    def setUp(self):
        super(ApiGatewayMiddleWareTest, self).setUp()

        ApiKey.objects.create(key='testapikey')

    def tearDown(self):
        ApiKey.objects.filter(key='testapikey').delete()

        super(ApiGatewayMiddleWareTest, self).tearDown()

    def test_process_request(self):
        basket_url = reverse('api-basket')

        # without Authorization header
        request = self.rf.get(basket_url)
        with self.assertRaises(PermissionDenied):
            ApiGatewayMiddleWare().process_request(request)

        # invalid Authorization header
        request = self.rf.get(basket_url, HTTP_AUTHORIZATION='wrongkey')
        with self.assertRaises(PermissionDenied):
            ApiGatewayMiddleWare().process_request(request)

        # valid Authorization header
        request = self.rf.get(basket_url, HTTP_AUTHORIZATION='testapikey')
        self.assertIsNone(ApiGatewayMiddleWare().process_request(request))

    def test_parse_session_id(self):
        dummy_request = DummyRequest()

        dummy_request.META['HTTP_SESSION_ID'] = 'SID:ANON:example.com:987171879'
        self.assertEqual(
            sorted(parse_session_id(dummy_request).items()),
            [('realm', 'example.com'), ('session_id', '987171879'), ('type', 'ANON')])

        dummy_request.META['HTTP_SESSION_ID'] = 'SID:AUTH:example.com:987171879'
        self.assertEqual(
            sorted(parse_session_id(dummy_request).items()),
            [('realm', 'example.com'), ('session_id', '987171879'), ('type', 'AUTH')])

        dummy_request.META['HTTP_SESSION_ID'] = 'SID:ANON:example.com:987171879-16EF'
        self.assertEqual(
            sorted(parse_session_id(dummy_request).items()),
            [('realm', 'example.com'), ('session_id', '987171879'), ('type', 'ANON')])

        dummy_request.META['HTTP_SESSION_ID'] = 'SID:ANON:example.com:98717-16EF:100'
        self.assertEqual(
            sorted(parse_session_id(dummy_request).items()),
            [('realm', 'example.com'), ('session_id', '98717'), ('type', 'ANON')])

        dummy_request.META['HTTP_SESSION_ID'] = 'SID:ANON::987171879'
        self.assertEqual(
            sorted(parse_session_id(dummy_request).items()),
            [('realm', ''), ('session_id', '987171879'), ('type', 'ANON')])

        dummy_request.META['HTTP_SESSION_ID'] = 'SID:ANON:example.com:923-thread1'
        self.assertEqual(
            sorted(parse_session_id(dummy_request).items()),
            [('realm', 'example.com'), ('session_id', '923-thread1'), ('type', 'ANON')])

        dummy_request.META['HTTP_SESSION_ID'] = 'SID:BULLSHIT:example.com:987171879'
        self.assertIsNone(parse_session_id(dummy_request))

        dummy_request.META['HTTP_SESSION_ID'] = 'ENTIREGABRBAGE'
        self.assertIsNone(parse_session_id(dummy_request))

        dummy_request.META['HTTP_SESSION_ID'] = 'SID:ANON:987171879'
        self.assertIsNone(parse_session_id(dummy_request))

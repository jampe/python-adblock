import adblock


def test_redirect_with_custom_resource():
    filters = adblock.FilterSet()
    filters.add_filter_list("-advertisement-$redirect=test\n")
    engine = adblock.Engine(filter_set=filters)
    engine.add_resources([("test", "application/javascript", "YWxlcnQoMSk=", None)])
    result = engine.check_network_urls(
        url="http://example.com/-advertisement-icon.",
        source_url="example.com",
        request_type="image",
    )
    assert result.matched
    assert not result.exception
    assert not result.important
    assert result.redirect == "data:application/javascript;base64,YWxlcnQoMSk="

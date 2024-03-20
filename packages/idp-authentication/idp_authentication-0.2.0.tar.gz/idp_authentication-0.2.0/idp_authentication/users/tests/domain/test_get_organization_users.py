def test_get_organization_users(container, user_2):
    get_organization_users_use_case = container.users_module().use_cases().get_organization_users()
    organization_users = get_organization_users_use_case.execute("Organization 1")
    assert organization_users == [user_2]

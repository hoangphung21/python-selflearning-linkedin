# # Using Arbitrary Keyword Arguments
def build_profile(first, last, **user_info):
    user_info['firstName'] = first
    user_info['lastName'] = last
    return user_info


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
for keys, values in user_profile.items():
    print(f"{keys}: {values}")

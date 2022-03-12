strong_password=input("enter a strong password:-")
if len(strong_password)>6 and len(strong_password)<16 and '$' in strong_password and '2' in strong_password or '8' in strong_password and "A" in strong_password or "Z" in strong_password:
    print("strong password:-",strong_password)
else:
    print("weak password")
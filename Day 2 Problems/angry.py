"""There are two friends, John and Smith, and the parameters j_angry and s_angry to indicate if each is angry. You are in trouble if both of them are angry or no one of them is angry.

Now, complete the function which returns true if you are in trouble, else return false"""

def friends_in_trouble(j_angry, s_angry):
    if j_angry == s_angry:
        return True
    else:
        return False
j_angry= input("Is J angry?(Yes/No)").strip().lower()
s_angry = input("Is S angry?(Yes/No)").strip().lower()
result = friends_in_trouble(j_angry,s_angry)
print("Mood:",result)
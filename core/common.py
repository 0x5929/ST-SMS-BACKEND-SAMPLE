# this file is for common utilities shared between apps, to further encourage DRY, But it does, however, contradict with the concept of independent apps

from authentication.models import Account
from rest_framework.exceptions import ValidationError

class UserEmailValidator:

    @classmethod
    def user_email_checker(cls, list_, reference, instance=None, partial=False):
        
        # PATCH
        if partial and list_:
            final_email_list = cls._user_check(list_, instance, reference)

        # PUT
        elif not partial and instance and list_:
            final_email_list = cls._user_check(list_, instance, reference)
        
        # POST
        elif not partial and not instance and list_:
            final_email_list = cls._user_check(list_, None, reference) 

        
        return final_email_list


    @classmethod
    def _user_check(cls, list_, instance, reference):
        final_list = []
        # UPDATES, ie PUT or PATCH
        if instance:
            # XOR operation between two lists will sort out their different elements
            diff = list(set(list_) ^ set(getattr(instance, reference)))
            
            final_diff = cls._email_filter(diff, raise_=True)
             
            # raise_ to false bc if users were deleted after the resource creation, we dont need to sent out 400 err, just silently take out the users who are not in database anymore
            final_original = cls._email_filter(getattr(instance, reference), raise_=False)

            final_list = final_diff + final_original

        # CREATES, ie POST
        else: 
            final_list = cls._email_filter(list_, raise_=True)

        return final_list

    @classmethod
    def _email_filter(lst, raise_=False):
        list_ = []

        # if we are trying to raise a validation error then if any of the email dont match what is available, return None so the validators in each app can raise
        if raise_:
            for email in lst:
                if not Account.objects.filter(email__exact=email).exists():
                    raise ValidationError(f'The user: {email} you are trying to add for access doesn\'t exist.')
                else:
                    list_.append(email)

        else:
            for email in lst:
                if Account.objects.filter(email__exact=email).exists():
                    list_.append(email)

        return list_
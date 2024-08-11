from Exercises.functions import random_fake_email_generator

emails = [
    "test.email+kevin@dailybyte.com",
    "test.e.mail+john.smith@dailybyte.com",
    "testemail+david@daily.byte.com"
]
my_emails = []

i = 0
while i < 1000:
    my_emails.append(random_fake_email_generator(1, 1, 1, 1, top_level_domains=["com"]))
    i += 1


def filter_unique_emails_count(emails_list):
    local_name_clean = ""
    cleaned_emails_list = []
    for email in emails_list:

        local_name_end_index = email.index("@")
        local_name = email[0:local_name_end_index]
        if "." in local_name:
            local_name = local_name.replace(".", "")
        if "+" in local_name:
            ignore_from_index = local_name.index("+")
            local_name = local_name[0:ignore_from_index]

        domain_name = email[local_name_end_index:]

        cleaned_email = (local_name + domain_name)
        # print(local_name + domain_name)
        if cleaned_email not in cleaned_emails_list:
            cleaned_emails_list.append(cleaned_email)

    count = len(cleaned_emails_list)

    return count


print("Unique Values: " + str(filter_unique_emails_count(my_emails)))

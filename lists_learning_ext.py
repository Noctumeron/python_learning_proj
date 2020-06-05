guest_names = []
next_word = 1
import random
print("Пора составить список гостей на выходные!")
while next_word == 1:
    new_word_1=input("Впиши сюда фио гостя, чтобы закончить набери 'стоп' - ")
    raw_words_1=new_word_1.lower()
    if raw_words_1 == 'стоп':
        next_word = 0
        for named_guest in guest_names:
            busy_check=random.random()
            print(busy_check)
            if busy_check >= 0.7:
                guest_names.remove(named_guest)
                message_2=f"Извини, но {named_guest.title()} не сможет присутствовать."
                replace_busy_guest=input(f"{message_2} Будем менять гостя? ")
                if replace_busy_guest == 'да':
                    new_word_2=input("Впиши сюда фио нового гостя - ")
                    raw_words_2=new_word_2.lower()
                    guest_names.append(raw_words_2.title())
                print("В списке: ", sorted(guest_names))
    else:
        formated_words_1=raw_words_1.title()
        guest_names.append(formated_words_1)
        message_1= f"Ты добавил {guest_names[-1]} в список гостей"
        print(message_1)

print("Удачного празднования!")

from classes.guest import Guest
from classes.song import Song
from classes.drink import Drink

class Room:

    def __init__(self, name, guests, song_list, capacity, entry_fee, till, drink_list):
        self.name = name
        self.guests = guests
        self.song_list = song_list
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.till = till
        self.drink_list = drink_list


    def count_guests_in_room(self):
        return len(self.guests)
    
    def check_guest_into_room(self, guest):
        if len(self.guests) > self.capacity:
            return "sorry, that room is full. Go HOME!!!"
        else:
            self.guests.append(guest)



    def check_out_guest_from_room(self, guest):
        self.guests.remove(guest)


    def pay_entry_fee(self, guest):
        guest.wallet -= self.entry_fee
        self.till += self.entry_fee

    def check_guest_into_room_and_pay(self, guest):
        if len(self.guests) > self.capacity:
            return "sorry, that room is full. Go HOME!!!"
        else:
            self.guests.append(guest)
            self.pay_entry_fee(guest)

    def add_song_to_playlist(self, song):
        self.song_list.append(song)

    def guest_fave_song_on_list(self, guest):
        for song in self.song_list:
            if song == guest.favourite_song:
                return "WooHoo"

    def sell_drink_to_guest(self, guest, drink):
        guest.wallet -= drink.price
        self.till += drink.price
        


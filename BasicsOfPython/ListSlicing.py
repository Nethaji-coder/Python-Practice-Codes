#list_name[start:end-1:steps]
li1 = [10,20,30,40,50,60]
sub_list = li1[0:4:1]
print(sub_list)#[10, 20, 30, 40]

sub_list1 = li1[::]
print(sub_list1)#[10, 20, 30, 40, 50, 60]

sub_list2 = li1[1::]
print(sub_list2)#[20, 30, 40, 50, 60]

sub_list3 = li1[::2]
print(sub_list3)#[10, 30, 50]

reverse_list = li1[::-1]
print(reverse_list)#[60, 50, 40, 30, 20, 10]

last_ele = li1[-1::]
print(last_ele)#[60]
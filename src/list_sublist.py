# class to implement nested list utilities
class listUtils:

    # method to sort a nested list basis 1st and 4th values of a sublist
    def Sort(sub_li):

        # iterate over the whole list
        l = len(sub_li)
        for i in range(0, l):
            for j in range(0, l-i-1):

                # sort by 1st value
                if (sub_li[j][0] > sub_li[j+1][0]):
                    tempo = sub_li[j]
                    sub_li[j]= sub_li[j + 1]
                    sub_li[j + 1]= tempo

                # if same first values, sort by $th value
                elif (sub_li[j][0] == sub_li[j+1][0]):
                    if (sub_li[j][3] > sub_li[j+1][3]):
                        tempo = sub_li[j]
                        sub_li[j]= sub_li[j + 1]
                        sub_li[j + 1]= tempo
        
        # return the sorted list
        return sub_li
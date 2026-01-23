1class Solution:
2    def reformatDate(self, date: str) -> str:
3        day, month, year = date.split()
4        day = day[:-2].zfill(2)
5        month_map = {
6            "Jan": "01", "Feb": "02", "Mar": "03",
7            "Apr": "04", "May": "05", "Jun": "06",
8            "Jul": "07", "Aug": "08", "Sep": "09",
9            "Oct": "10", "Nov": "11", "Dec": "12"
10        }
11
12        return f"{year}-{month_map[month]}-{day}"
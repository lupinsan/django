from django.utils.safestring import mark_safe
import copy

class Pagination(object):

    def __init__(self, request, total_count):
        page = request.GET.get('page', "1")
        if not page.isdecimal():
            page = 1
        else:
            page = int(page)
            if page < 1:
                page = 1
        self.page = page

        self.start = (page - 1) * 10
        self.end = page * 10

        self.total_count = total_count
        total_page_count, div = divmod(total_count, 10)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count

        self.query_dict = copy.deepcopy(request.GET)
        self.query_dict._mutable = True

    def html(self):
        paper_list = []

        if self.total_page_count <= 11:
            paper_start = 1
            paper_end = self.total_page_count + 1
        else:
            if page <= 5:
                paper_start = 1
                paper_end = 11 + 1
            else:
                if page + 5 > self.total_page_count:
                    paper_start = self.total_page_count - 10
                    paper_end = self.total_page_count + 1
                else:
                    paper_start = self.page - 5
                    paper_end = self.page + 5 + 1

        for i in range(paper_start, paper_end):
            self.query_dict.setlist("page",[i])
            query = self.query_dict.urlencode()
            if i == self.page:
                element = '<li class="active"><a href="?{0}">{1}</a></li>'.format(query,i)
            else:
                element = '<li><a href="?{0}">{1}</a></li>'.format(query, i)
            paper_list.append(element)

        paper_string = mark_safe("".join(paper_list))
        return paper_string

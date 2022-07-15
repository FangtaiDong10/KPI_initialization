from werkzeug.exceptions import HTTPException

def paginate(query_set, page_num, per_page=10):
    """
    Paginate a query set.
    :param query_set: Query set to paginate.
    :param page_num: Page number.
    :param per_page: Number of items per page.
    :return: Paginated query set.
    """
    try:
        paginated_objects = query_set.paginate(page_num, per_page)

        return {
            # total pages exists
            "total_pages": paginated_objects.pages,

            # total items exists
            "counts": paginated_objects.total,

            # current page number
            "page_num": page_num,

            "items" : [obj.to_dict() for obj in paginated_objects.items],
        }
    except HTTPException as e:
        if e.code == 404:
            return {"message": f"Page {page_num} was not found"}, 404
        else:
            raise e # re-raise the exception
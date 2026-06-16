# pdf_utils.py

import io
import re

from pypdf import PdfReader, PdfWriter


def get_total_pages(reader: PdfReader) -> int:
    """
    Return total number of pages in PDF.
    """
    return len(reader.pages)


def parse_page_range(page_range: str, total_pages: int) -> tuple[int, int]:
    """
    Convert strings like:

        "5-10"
        "7"
        "1-"

    into:

        (5,10)
        (7,7)
        (1,total_pages)
    """

    page_range = page_range.strip()

    if "-" not in page_range:
        page = int(page_range)

        if page < 1 or page > total_pages:
            raise ValueError(f"Page {page} out of range (1-{total_pages})")

        return page, page

    start_str, end_str = page_range.split("-", maxsplit=1)

    start_page = int(start_str)

    if end_str == "":
        end_page = total_pages
    else:
        end_page = int(end_str)

    if start_page < 1:
        raise ValueError("Pages are 1-indexed.")

    if end_page > total_pages:
        raise ValueError(f"Page {end_page} exceeds total pages ({total_pages})")

    if start_page > end_page:
        raise ValueError(f"Invalid range {start_page}-{end_page}")

    return start_page, end_page


def extract_page_range(
    reader: PdfReader,
    start_page: int,
    end_page: int,
) -> bytes:
    """
    Extract inclusive page range as standalone PDF bytes.
    """

    writer = PdfWriter()

    for i in range(start_page - 1, end_page):
        writer.add_page(reader.pages[i])

    buffer = io.BytesIO()
    writer.write(buffer)

    return buffer.getvalue()


def extract_pages_to_pdf_bytes(
    reader: PdfReader,
    pages: list[int],
) -> bytes:
    """
    Extract arbitrary pages.

    Example:
        [1,2,5,7]
    """

    writer = PdfWriter()

    for page_num in sorted(set(pages)):
        writer.add_page(reader.pages[page_num - 1])

    buffer = io.BytesIO()
    writer.write(buffer)

    return buffer.getvalue()


def full_pdf_bytes(reader: PdfReader) -> bytes:
    """
    Serialize entire PDF to bytes.
    """

    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    buffer = io.BytesIO()
    writer.write(buffer)

    return buffer.getvalue()


def build_batches(
    start_page: int,
    end_page: int,
    batch_size: int,
    overlap: int,
):
    """
    Example:

        start=1
        end=17
        batch_size=6
        overlap=1

    yields:

        (1,6)
        (6,11)
        (11,16)
        (16,17)
    """

    current = start_page

    while current <= end_page:

        batch_end = min(
            current + batch_size - 1,
            end_page,
        )

        yield current, batch_end

        if batch_end == end_page:
            break

        current = batch_end - overlap + 1

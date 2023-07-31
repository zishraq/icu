student_id_regex = r'^\d{4}\-\d\-\d{2}\-\d{3}$'
ADDED = 'added'
DROPPED = 'dropped'
PENDING = 'pending'
APPROVED = 'approved'
REJECTED = 'rejected'
REQUEST_APPROVED = 'request_approved'
MALE = 'male'
FEMALE = 'female'
OTHER = 'other'


def get_referer_parameter(request):
    referer = str(request.META.get('HTTP_REFERER'))
    split_referer = referer.split('/')
    referer_parameter = split_referer[-1]

    if not referer_parameter:
        referer_parameter = split_referer[-2]

    return referer_parameter


def get_referer_url(request):
    referer = str(request.META.get('HTTP_REFERER'))
    print(referer)

    return referer


def text_shorten(text: str, length):
    if length >= len(text):
        return text

    filtered_text = text[:length]

    last_full_word = filtered_text.rfind(' ')
    filtered_text = str(
        text[:last_full_word] + '...'
    ).strip()
    return filtered_text


def get_conflicting_sections_with_requested_section(previous_selected_sections, selected_section):
    selected_course = selected_section.course

    conflicting_sections = {}
    section_ids = []

    for previous_section in previous_selected_sections:
        if previous_section.section.course == selected_course or selected_section.does_conflict_with_section(previous_section.section):
            section_ids.append(previous_section.section.section_id)
            conflicting_sections[previous_section.section.course.course_code] = previous_section.section.section_no

    return {
        'section_ids': section_ids,
        'conflicting_sections': conflicting_sections
    }

class DataHelper:

    @classmethod
    def data_conversion(cls, model, STUDENT_RECORD_HEADERS):
        data = {}

        for header in STUDENT_RECORD_HEADERS:
            if header == 'graduate' or \
                    header == 'passed_first_exam' or \
                    header == 'passed_second_or_third_exam' or \
                    header == 'employed':

                data[header] = cls.bool_conversion(model, header)

            elif header == 'start_date' or \
                    header == 'completion_date' or \
                    header == 'date_enrollment_agreement_signed':

                data[header] = cls.date_conversion(model, header)

            elif header == 'course_cost' or \
                    header == 'total_charges_charged' or \
                    header == 'total_charges_paid' or \
                    header == 'starting_wage':

                data[header] = cls.money_conversion(model, header)

            else:
                data[header] = str(getattr(model, header))

        return data

    @staticmethod
    def bool_conversion(model, header):
        value = getattr(model, header)
        return 'Y' if value else ''

    @staticmethod
    def date_conversion(model, header):

        date_obj = getattr(model, header)
        return '%s/%s/%s' % (str(date_obj.day), str(date_obj.month), str(date_obj.year))

    @staticmethod
    def money_conversion(model, header):

        money_obj = getattr(model, header)
        return '$%s' % str(money_obj.amount)

    # NOTE data keys are assigned by each item inside STUDENT_RECORD_HEADERS,
    # by logic, as long as we dont change and or mess with the way data_conversion and clean_data,
    # order of dict is preserved by assignment by 3.6!
    @staticmethod
    def finalize_data(data):
        return [value for value in data.values()]

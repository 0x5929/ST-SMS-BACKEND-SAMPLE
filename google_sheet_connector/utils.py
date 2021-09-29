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
        # can i get rid of bool()? test in shell plz
        return 'Y' if bool(getattr(model, header)) else ''

    @staticmethod
    def date_conversion(date_obj):

        # convert date_obj into string google sheet can easily understand and
        # return string
        pass

    @staticmethod
    def money_conversion(money_obj):

        # convert money_obj into string google sheet can easily understand and
        # return string
        pass

    # NOTE data keys are assigned by each item inside STUDENT_RECORD_HEADERS,
    # by logic, as long as we dont change and or mess with the way data_conversion and clean_data,
    # order of dict is preserved by assignment by 3.6!
    @staticmethod
    def finalize_data(data):
        return [value for value in data.values()]

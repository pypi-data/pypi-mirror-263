class StatisticCalculator:
    def __init__(
        self,
        norm_res,
        norm_ved,
        norm_volume,
        norm_time,
        norm_seq,
        not_res,
        not_ved,
        not_volume,
        not_time,
        not_seq,
    ):
        self.norm_res = norm_res
        self.norm_ved = norm_ved
        self.norm_volume = norm_volume
        self.norm_time = norm_time
        self.norm_seq = norm_seq
        self.not_res = not_res
        self.not_ved = not_ved
        self.not_volume = not_volume
        self.not_time = not_time
        self.not_seq = not_seq

    def get_statistic_for_properties_and_all_stat(self):
        result_dict = dict()
        result_dict["percentage_of_normal_resource_volume_values"] = round(
            self.norm_res
        )
        result_dict["percentage_of_normal_resources_according_to_journal"] = round(
            self.norm_ved
        )
        result_dict["percentage_of_normal_work_time_values"] = round(self.norm_time)
        result_dict["percentage_of_normal_work_volume_values"] = round(self.norm_volume)
        result_dict["percentage_of_normal_work_connection_values"] = round(
            self.norm_seq
        )
        result_dict["percentage_of_normal_values_across_all_works"] = round(
            (self.norm_time + self.norm_volume + self.norm_seq) / 3
        )
        result_dict["percentage_of_normal_values_across_all_resources"] = round(
            (self.norm_res + self.norm_ved) / 2
        )
        return result_dict

    def get_plan_statistic(self):
        norm_value = round(
            (
                self.norm_res
                + self.norm_ved
                + self.norm_volume
                + self.norm_time
                + self.norm_seq
            )
            / 5
        )
        not_val = round(
            (
                self.not_res
                + self.not_ved
                + self.not_volume
                + self.not_time
                + self.not_seq
            )
            / 5
        )
        tested_val = 100 - not_val
        dict_result = {
            "percentage_of_normal_plan_values": norm_value,
            "percentage_of_plan_values_covered_by_validation": tested_val,
        }

        return dict_result

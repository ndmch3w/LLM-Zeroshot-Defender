import pandas as pd


class Analysis:
    def get_tpr_fnr(self, original_csv, filtered_csv):
        df_original = pd.read_csv(original_csv)
        df_filtered = pd.read_csv(filtered_csv)
        count_tp = 0
        count_fn = 0
        predicted_yes = 0

        for item1, item2 in zip(df_original['is harmful?'], df_filtered['is harmful?']):
            if item1 == "Yes":
                predicted_yes += 1
                if item2.lower().strip().startswith("no") != True:
                    count_tp += 1
                else:
                    count_fn += 1

        true_positive_rate = count_tp/predicted_yes
        false_negative_rate = count_fn/predicted_yes

        return true_positive_rate, false_negative_rate
    
    def get_stats_init_data(self, original_csv):
        df_original = pd.read_csv(original_csv)
        total_responses = df_original['is harmful?'].size
        print("Total responses: " + str(total_responses))
        total_yes = 0
        for item in df_original['is harmful?']:
            if item == "Yes":
                total_yes += 1
        total_no = total_responses - total_yes
        print("Harmful responses: ", total_yes)
        print("Benign responses: ", total_no)
        


if __name__ == "__main__":
    analysis = Analysis()
    (tpr, fnr) = analysis.get_tpr_fnr("data/all_repsonses_gpt.csv", \
                                      "data/filtered_gpt_by_llama13bitq8.csv")
    print("True Positive Rate: ", tpr) 
    print("False Negative Rate: ", fnr) 

    print(analysis.get_stats_init_data("data/all_repsonses_llama.csv"))

# LLaMA 7b quantized 8

# For gpt_responses (52 harmful, 50 benign):
#tpr: 0.6923076923076923
#fnr: 0.3076923076923077

# For llama_responses (58 harmful, 50 benign):
# True Positive Rate:  0.8653846153846154 
# False Negative Rate:  0.1346153846153846

# ------------------------------------------------

# LLAMA 13 bit quantized 4 (for gpt responses)
# tpr: 0.5
# fnr: 0.5

# LLAMA 13 bit quantized 4 (for llama responses)
# tpr: 0.5344827586206896 
# fnr: 0.46551724137931033

import pandas as pd
from lifelines import KaplanMeierFitter
from lifelines.statistics import logrank_test
from lifelines import CoxPHFitter
from geney import unload_pickle, unload_json, access_conservation_data
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)

epistasis_frequency_data = unload_pickle('/tamir2/nicolaslynn/projects/mutation_colabs/data/epistasis2case_tracker.pkl')
mutation_frequency_data = pd.Series(unload_json('/tamir2/nicolaslynn/projects/TCGAParsed/recurring_single_muts_tcga.json'))

def prepare_clinical_data():
    CLINICAL_DATA_FILE = Path('/tamir2/yoramzar/Projects/Cancer_mut/Explore_data/reports/df_p_all.pkl')
    df = unload_pickle(CLINICAL_DATA_FILE)
    df.rename(columns={'patient_uuid': 'case_id'}, inplace=True)
    cols = list(df.columns)
    cols_days_to_followup = [col for col in cols if 'days_to_followup' in col] + [col for col in cols if 'days_to_last_followup' in col]
    cols_days_to_know_alive = [col for col in cols if 'days_to_know_alive' in col] + [col for col in cols if 'days_to_last_known_alive' in col]
    cols_days_to_death = [col for col in cols if 'days_to_death' in col]
    cols_duration = cols_days_to_followup + cols_days_to_know_alive + cols_days_to_death
    col_vital_status = 'days_to_death'
    event_col_label = 'event'
    duration_col_label = 'duration'
    df.insert(1, event_col_label, df.apply(lambda x: int(not np.isnan(x[col_vital_status])), axis=1))
    df.insert(1, duration_col_label, df.apply(lambda x: max([x[col] for col in cols_duration if not np.isnan(x[col])], default=-1), axis=1))
    df[duration_col_label] /= 365
    df = df.query(f"{duration_col_label}>=0.0")[['duration', 'event', 'case_id', 'chemotherapy', 'hormone_therapy', 'immunotherapy', 'targeted_molecular_therapy', 'Proj_name']]
    df.to_csv('/tamir2/nicolaslynn/data/tcga_metadata/tcga_clinical_data.csv')
    return df


class SurvivalAnalyzer:
    def __init__(self, clinical_df):
        self.clinical_df = clinical_df

    def perform_cox_analysis(self, pid1, pid2):
        df1 = self.clinical_df.query(f"case_id in {pid1}")
        df2 = self .clinical_df.query(f"case_id in {pid2}")
        df1['group'] = 1
        df2['group'] = 2
        df = pd.concat([df1, df2])
        cph = CoxPHFitter().fit(df, 'T', 'E')
        cph.print_summary()

    def plot_cox_covariate(self, pid1, pid2, covariate):
        df1 = self.clinical_df.query(f"case_id in {pid1}")
        df2 = self.clinical_df.query(f"case_id in {pid2}")
        df1['group'] = 1
        df2['group'] = 2
        df = pd.concat([df1, df2])
        cph = CoxPHFitter().fit(df, 'T', 'E')
        cph.plot_partial_effects_on_outcome(covariates=covariate, cmap='coolwarm')

    def km_significance(self, pid1, pid2):
        affected_df, nonaffected_df = self.clinical_df.query(f"case_id in {pid1}"), self.clinical_df.query(f"case_id in {pid2}")

        if affected_df.empty or nonaffected_df.empty:
            return np.nan, np.nan, np.nan

        results = logrank_test(affected_df['duration'], nonaffected_df['duration'],
                               event_observed_A=affected_df['event'],
                               event_observed_B=nonaffected_df['event'])

        p_value = results.p_value
        kmf = KaplanMeierFitter()
        kmf.fit(affected_df['duration'], affected_df['event'], label=f'With Epistasis ({len(affected_df)})')
        times, surv_probs = kmf.survival_function_.index.values, kmf.survival_function_.values.flatten()
        auc1 = np.trapz(surv_probs, times)
        kmf.fit(nonaffected_df['duration'], nonaffected_df['event'], label=f'Without Epistasis ({len(nonaffected_df)})')
        times, surv_probs = kmf.survival_function_.index.values, kmf.survival_function_.values.flatten()
        auc2 = np.trapz(surv_probs, times)
        return p_value, auc1, auc2

    def km_plot(self, pid1, pid2):
        affected_df, nonaffected_df = self.clinical_df.query(f"case_id in {pid1}"), self.clinical_df.query(f"case_id in {pid2}")

        results = logrank_test(affected_df['duration'], nonaffected_df['duration'],
                               event_observed_A=affected_df['event'],
                               event_observed_B=nonaffected_df['event'])

        p_value = results.p_value
        kmf = KaplanMeierFitter()
        # Fit data
        kmf.fit(affected_df['duration'], affected_df['event'], label=f'Without Epistasis ({len(affected_df)})')
        ax = kmf.plot()

        kmf.fit(nonaffected_df['duration'], nonaffected_df['event'], label=f'With Epistasis ({len(nonaffected_df)})')
        kmf.plot(ax=ax)
        plt.text(5, 0.95, f'pval: {p_value:.3e}')
        plt.show()
        return p_value

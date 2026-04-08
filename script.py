import pandas as pd
import plotly.express as px
from scipy import stats

inputdir = 'bank.csv'

class process_dataset:
    def __init__(self, inputdir:str):
        self.data_frame = pd.read_csv(inputdir, sep=';')
        self.info_columns = {i:{'datatype':self.data_frame[i].dtypes.name,
                                'n_nulls':list(self.data_frame.isnull().sum())[n]} 
                                for n, i in enumerate(self.data_frame.columns)}
        self.counts = self.data_frame['y'].value_counts()
        self.values = self.data_frame['y'].unique()
        self.graphical_representation = px.pie(self.counts, names=self.counts.index, values='count', hole=0.4)
        self.plot_initialfig()
    
    def plot_initialfig(self):
        self.graphical_representation.write_image(f'Porcentage aceptation.png')
        self.graphical_representation.show()
    
    def calculating_porcentage_yes_bygroup(self, column_value:str):
        filter_data = self.data_frame[self.data_frame['y'] == 'yes']
        resume_data = filter_data.groupby(column_value)['y'].agg(total_yes = 'count')
        resume_data['%'] = 100.0*resume_data['total_yes']/self.counts['yes']
        resume_data['%'] = resume_data['%'].round(2)
        return resume_data.sort_values(by='%', ascending=False)
    
    def pie_graph(self, column_value:str):
        resume_data = self.calculating_porcentage_yes_bygroup(column_value)
        fig = px.pie(
            resume_data,
            names = resume_data.index,
            values = 'total_yes',
            hole = 0.4
        )
        fig.update_layout(title_text = f'Porcentage aceptation per {column_value}')
        fig.write_image(f'pie_{column_value}.png')
        fig.show()
    
    def plotbox_graph(self, column_value:str): 
        fig = px.box(self.data_frame, x='y', y=column_value, points='all', log_y=True)
        fig.write_image(f'boxes_{column_value}.png')
        fig.show()
    
    def plotline_graph(self, column_value:str):
        table_resume = self.calculating_porcentage_yes_bygroup(column_value)
        table_resume = table_resume.sort_values(by=column_value, ascending=True)
        fig = px.line(table_resume, x = table_resume.index, y = '%', title=f'Porcentage aceptation per {column_value}')
        fig.write_image(f'line_{column_value}.png')
        fig.show()

    def apply_hipotesis_test(self, column_value:str):
        groups_y = [self.data_frame[self.data_frame['y'] == value][column_value] for value in self.values]
        r = stats.kruskal(*groups_y)
        return r
    
    def grouping_data(self, column_value:str):
        return self.data_frame.groupby('y')[column_value].mean()
    
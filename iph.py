# 1. Import Dash
import  pandas as pd
import dash
import dash_bootstrap_components as dbc
from dash import html, Input, Output, State,dcc
import tensorflow.python.util.deprecation as deprecation
deprecation._PRINT_DEPRECATION_WARNINGS = False
 
import joblib
ss = joblib.load('Scaler')
from tensorflow.keras.models import load_model
from keras import backend
import tensorflow as tf
global graph,model,sess
tf.compat.v1.disable_eager_execution()
graph = tf.compat.v1.get_default_graph()#为了清楚缓存
sess=backend.get_session()

model2 = load_model('model.h5')
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.FLATLY],suppress_callback_exceptions=True)
server = app.server
# 2. Create a Dash app instance



app.layout = html.Div([
        dbc.Navbar(#导航栏
        dbc.Container(
            [
                html.A(
                    # Use row and col to control vertical alignment of logo / brand
                    dbc.Row(
                        [dbc.Col(dbc.NavbarBrand(children=[html.H5("Calculation Tool for isolated post-challenge hyperglycemia(IPH)"),
                            html.H5("单纯餐后血糖升高的计算工具")],className="ms-2")),
                        ],
                        align="center",
                        className="g-0",
                    ),
                    style={"textDecoration": "none"},
                ),
                dcc.Tabs(id="tabs-example-graph", value='tab-1-example-graph', children=[
                    dcc.Tab(label='English', value='tab-1-example-graph'),
                    dcc.Tab(label='中文', value='tab-2-example-graph'),
                ],style={
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}),
            ]
        ),
    color="dark",
    dark=True,
),html.Div(id='tabs-content-example-graph')],style={"margin-left": "175px","margin-right": "175px"}
)

@app.callback(Output('tabs-content-example-graph', 'children'),
              Input('tabs-example-graph', 'value'))

def Language(tab):
    if tab == 'tab-1-example-graph':
        return html.Div(
            [dbc.Container(children=[
                html.Div(children=[
                    html.Div(children=
                    [html.H4("Basic information"),
                     dbc.Form(children=[dbc.Row(
    [
        dbc.Label("Age (year)", html_for="age", width=7),
        dbc.Col(children=[
            dbc.Input(
                type="number",
                id="age",
                placeholder="20-120 ",
                min=20,
                max=120
            ),
            dbc.FormFeedback(
                "Please enter a value between 18 and 120",
                type="invalid")],
            width=4,
        ),
    ],
    className="mb-3",
)
, dbc.Row(
    [
        dbc.Label("Height (cm)", html_for="Height", width=7),
        dbc.Col(
            dbc.Input(
                type="number",
                id="height",
                placeholder="120-220",
                min=120,
                max=220
            ),
            width=4,
        ),
    ],
    className="mb-3",
),

dbc.Row(
    [
        dbc.Label("Weight (kg)", html_for="weight", width=7),
        dbc.Col(
            dbc.Input(
                type="number",
                id="weight",
                placeholder="40-150 ",
                min=40,
                max=150
            ),
            width=4,
        ),
    ],
    className="mb-3",
),

dbc.Row(
    [
        dbc.Label("Heart rate (BMP)", html_for="HR", width=7),
        dbc.Col(
            dbc.Input(
                type="number",
                id="hr",
                placeholder="40-220",
                min=40,
                max=220
            ),
            width=4,
        ),
    ],
    className="mb-3",
),

dbc.Row(
    [
        dbc.Label("Systolic blood pressure (SBP, mmHg)", html_for="SBP", width=7),
        dbc.Col(
            dbc.Input(
                type="number",
                id="sbp",
                placeholder="70-200",
                min=70,
                max=200
            ),
            width=4,
        ),
    ],
    className="mb-3",
)])],
                             style={'padding': 10, 'flex': 1}),
                    html.Div(children=
                             [html.H4("Blood index"),
                              dbc.Form(children=[dbc.Row(
    [
        dbc.Label("Fasting plasma glucose(FPG, mmol/L)", html_for="FPG", width=8),
        dbc.Col(
            dbc.Input(
                type="number",
                id="fpg",
                placeholder="4-16 ",#正常人血糖下限为3.9
                min=3.9,
                max=16
            ),
            width=4,
        ),
    ],
    className="mb-3",
),

dbc.Row(
    [
        dbc.Label("Hemoglobin A1c(HbA1c, %)", html_for="HbA1c", width=8),
        dbc.Col(
            dbc.Input(
                type="number",
                id="hba1c",
                placeholder="3-15 ",
                min=3.0,
                max=15.1
            ),
            width=4,
        ),
    ],
    className="mb-3",
),


dbc.Row(
    [
        dbc.Label("Alanine transaminase(ALT, U/L)", html_for="ALT", width=8),
        dbc.Col(
            dbc.Input(
                type="number",
                id="alt",
                placeholder="0-1200 ",
                min=0,
                max=1200
            ),
            width=4,
        ),
    ],
    className="mb-3",
),

dbc.Row(
    [
        dbc.Label("Triglyceride(TG, mmol/L)", html_for="TG", width=8),
        dbc.Col(
            dbc.Input(
                type="number",
                id="tg",
                placeholder="0-76 ",
                min=0,
                max=76
            ),
            width=4,
        ),
    ],
    className="mb-3",
),

dbc.Row(
    [
        dbc.Label("High-density lipoprotein cholesterol(HDL-C, mmol/L)", html_for="HDL", width=8),
        dbc.Col(
            dbc.Input(
                type="number",
                id="hdl",
                placeholder="0.5-4 ",
                min=0.5,
                max=4
            ),
            width=4,
        ),
    ],
    className="mb-3",
),

dbc.Row(
    [
        dbc.Label("Low-density lipoprotein cholesterol(LDL-C, mmol/L)", html_for="LDL", width=8),
        dbc.Col(
            dbc.Input(
                type="number",
                id="ldl",
                placeholder="0-7 ",
                min=0.1,
                max=7
            ),
            width=4,
        ),
    ],
    className="mb-3",
)])],
                             style={'padding': 10, 'flex': 1})], style={'display': 'flex', 'flex-direction': 'row'})], id="form1"),
                html.Button("Calculate", n_clicks=0, className="me-1", id="Caculate1", style={"background-color": '#778899',  'color': 'white', 'font-size': '24px','border-radius': '12px','text-align': 'center','text-decoration': 'none'}),
                html.Br(),
                html.Br(),
                html.H6("Cut off:【0.079】       ",style={'font-size': '20px'}),
                html.Div(id="output-value2",style={'font-size': '20px'}),
                html.Br(),
            ])
    elif tab == 'tab-2-example-graph':
        return html.Div(
            [dbc.Container(children=[
                html.Div(children=[
                    html.Div(children=
                             [html.H4("基本信息"),
                              dbc.Form(children=[dbc.Row(
                                  [
                                      dbc.Label("年龄 (岁)", html_for="age", width=7),
                                      dbc.Col(children=[
                                          dbc.Input(
                                              type="number",
                                              id="age1",
                                              placeholder="20-120 ",
                                              min=20,
                                              max=150
                                          ),
                                          dbc.FormFeedback(
                                              "Please enter a value between 18 and 120",
                                              type="invalid")],
                                          width=4,
                                      ),
                                  ],
                                  className="mb-3",
                              )
                                  , dbc.Row(
                                      [
                                          dbc.Label("身高 （厘米）", html_for="Height", width=7),
                                          dbc.Col(
                                              dbc.Input(
                                                  type="number",
                                                  id="height1",
                                                  placeholder="120-220 ",
                                                  min=120,
                                                  max=220
                                              ),
                                              width=4,
                                          ),
                                      ],
                                      className="mb-3",
                                  ),

                                  dbc.Row(
                                      [
                                          dbc.Label("体重 （千克）", html_for="weight", width=7),
                                          dbc.Col(
                                              dbc.Input(
                                                  type="number",
                                                  id="weight1",
                                                  placeholder="35-150 ",
                                                  min=35,
                                                  max=150
                                              ),
                                              width=4,
                                          ),
                                      ],
                                      className="mb-3",
                                  ),

                                  dbc.Row(
                                      [
                                          dbc.Label("心率 （每秒心跳次数）", html_for="HR", width=7),
                                          dbc.Col(
                                              dbc.Input(
                                                  type="number",
                                                  id="hr1",
                                                  placeholder="40-120",
                                                  min=40,
                                                  max=120
                                              ),
                                              width=4,
                                          ),
                                      ],
                                      className="mb-3",
                                  ),

                                  dbc.Row(
                                      [
                                          dbc.Label("收缩压 （SBP，毫米汞柱）", html_for="SBP", width=7),
                                          dbc.Col(
                                              dbc.Input(
                                                  type="number",
                                                  id="sbp1",
                                                  placeholder="70-200 ",
                                                  min=70,
                                                  max=200
                                              ),
                                              width=4,
                                          ),
                                      ],
                                      className="mb-3",
                                  )])],
                             style={'padding': 10, 'flex': 1}),
                    html.Div(children=
                             [html.H4("血液指标"),
                              dbc.Form(children=[dbc.Row(
                                  [
                                      dbc.Label("空腹血糖 （FPG，毫摩尔每升）", html_for="FPG", width=8),
                                      dbc.Col(
                                          dbc.Input(
                                              type="number",
                                              id="fpg1",
                                              placeholder="4-16",
                                              min=4,
                                              max=16
                                          ),
                                          width=4,
                                      ),
                                  ],
                                  className="mb-3",
                              ),

                                  dbc.Row(
                                      [
                                          dbc.Label("糖化血红蛋白 （HbA1c，%）", html_for="HbA1c", width=8),
                                          dbc.Col(
                                              dbc.Input(
                                                  type="number",
                                                  id="hba1c1",
                                                  placeholder="3-15",
                                                  min=3.0,
                                                  max=15.1
                                              ),
                                              width=4,
                                          ),
                                      ],
                                      className="mb-3",
                                  ),

                                  dbc.Row(
                                      [
                                          dbc.Label("谷丙转氨酶 （ALT，单位每升）", html_for="ALT", width=8),
                                          dbc.Col(
                                              dbc.Input(
                                                  type="number",
                                                  id="alt1",
                                                  placeholder="0-1200",
                                                  min=0,
                                                  max=1200
                                              ),
                                              width=4,
                                          ),
                                      ],
                                      className="mb-3",
                                  ),

                                  dbc.Row(
                                      [
                                          dbc.Label("甘油三脂 （TG，毫摩尔每升）", html_for="TG", width=8),
                                          dbc.Col(
                                              dbc.Input(
                                                  type="number",
                                                  id="tg1",
                                                  placeholder="0-76 ",
                                                  min=0.1,
                                                  max=42
                                              ),
                                              width=4,
                                          ),
                                      ],
                                      className="mb-3",
                                  ),

                                  dbc.Row(
                                      [
                                          dbc.Label("高密度脂蛋白 （HDL-C，毫摩尔每升）", html_for="HDL", width=8),
                                          dbc.Col(
                                              dbc.Input(
                                                  type="number",
                                                  id="hdl1",
                                                  placeholder="0.5-4 ",
                                                  min=0,
                                                  max=17
                                              ),
                                              width=4,
                                          ),
                                      ],
                                      className="mb-3",
                                  ),

                                  dbc.Row(
                                      [
                                          dbc.Label("低密度脂蛋白 （LDL-C，毫摩尔每升）", html_for="LDL", width=8),
                                          dbc.Col(
                                              dbc.Input(
                                                  type="number",
                                                  id="ldl1",
                                                  placeholder="0-7 ",
                                                  min=0,
                                                  max=7
                                              ),
                                              width=4,
                                          ),
                                      ],
                                      className="mb-3",
                                  )])],
                             style={'padding': 10, 'flex': 1})], style={'display': 'flex', 'flex-direction': 'row'})],
                id="form1"),
        html.Button("计算", n_clicks=0, className="me-1", id="Caculate2", style={"background-color": '#778899',  'color': 'white', 'font-size': '24px','border-radius': '12px','text-align': 'center','text-decoration': 'none'}),
        html.Br(),
        html.Br(),
        html.H6("阈值:【0.079】       ", style={'font-size': '20px'}),
        html.Div(id="output-value3", style={'font-size': '20px'} ),
        html.Br(),
        ])


@app.callback(
    Output(component_id='output-value2', component_property='children'),
    [Input('Caculate1', 'n_clicks'),
     State('age', 'value'),
     State('height', 'value'),
     State('weight', 'value'),
     State('hr', 'value'),
     State('sbp', 'value'),
     State('fpg', 'value'),
     State('hba1c','value'),
     State('alt', 'value'),
     State('tg', 'value'),
     State('hdl', 'value'),
     State('ldl', 'value')],
    prevent_initial_call=True )


def input_to_output(n_clicks,age, height, weight, hr, sbp, fpg, hba1c, alt, tg, hdl, ldl):
    if n_clicks:
        if age is None:
            age = 57.7
        else:
            age = age
        if height is None:
            height =160.6
        else:
            height = height
        if weight is None:
            weight = 64.2
        else:
            weight = weight
        if hr is None:
            hr = 79.1
        else:
            hr = hr
        if sbp is None:
            sbp = 130.6
        else:
            sbp = sbp
        if fpg is None:
            fpg = 5.45
        else:
            fpg = fpg
        if hba1c is None:
            hba1c = 5.81
        else:
            hba1c = hba1c
        if alt is None:
            alt = 16.0
        else:
            alt = alt
        if tg is None:
            tg = 1.30
        else:
            tg = tg
        if ldl is None:
            ldl = 3.08
        else:
            ldl = ldl
        if hdl is None:
            hdl = 1.38
        else:
            hdl = hdl
        bmi = (weight) / ((height / 100) ** 2)
        # 预测数据  字典转成数据框
        c = {"Glu0": fpg,
             "HbAlc": hba1c,
             "bmi": bmi,
             "age": age,
             "hr": hr,
             "ALT": alt,
             "TG": tg,
             "LDL": ldl,
             "sbp": sbp,
             "HDL": hdl
             }  # 将列表a，b转换成字典
        test = pd.DataFrame(c, index=[0])  # 将字典转换成为数据框
        test1 = ss.transform(test.values)
        test2 = pd.DataFrame(test1, columns=test.columns)
        test2= test2[['Glu0', "HbAlc", "HDL", "age", "hr", "ALT", "TG", "LDL", "sbp", "bmi"]]
        with sess.as_default():
            with graph.as_default():
                testreslut = model2.predict(test2)
                re = round(testreslut[0, 0], 4)
                if re>=0.079:
                    return u"The probability of IPH：【{:.4f}】       Suggest:Please further test postprandial blood glucose".format(re)
                else:
                    return u"The probability of IPH：【{:.4f}】 ".format(re)
             


@app.callback(
    Output(component_id='output-value3', component_property='children'),
    [Input('Caculate2', 'n_clicks'),
     State('age1', 'value'),
     State('height1', 'value'),
     State('weight1', 'value'),
     State('hr1', 'value'),
     State('sbp1', 'value'),
     State('fpg1', 'value'),
     State('hba1c1','value'),
     State('alt1', 'value'),
     State('tg1', 'value'),
     State('hdl1', 'value'),
     State('ldl1', 'value')],
     prevent_initial_call=True)




def input_to_output2(n_clicks1,age1, height1, weight1, hr1, sbp1, fpg1, hba1c1, alt1, tg1, hdl1, ldl1):
    if n_clicks1:
        if age1 is None:
            age = 57.1
        else:
            age = age1
        if height1 is None:
            height = 160.6
        else:
            height = height1
        if weight1 is None:
            weight = 62.2
        else:
            weight = weight1
        if hr1 is None:
            hr = 79.1
        else:
            hr = hr1
        if sbp1 is None:
            sbp = 130.6
        else:
            sbp = sbp1
        if fpg1 is None:
            fpg = 5.45
        else:
            fpg = fpg1
        if hba1c1 is None:
            hba1c = 5.81
        else:
            hba1c = hba1c1
        if alt1 is None:
            alt = 16.0
        else:
            alt = alt1
        if tg1 is None:
            tg = 1.30
        else:
            tg = tg1
        if ldl1 is None:
            ldl = 3.08
        else:
            ldl = ldl1
        if hdl1 is None:
            hdl = 1.38
        else:
            hdl = hdl1
        bmi = (weight) / ((height / 100) ** 2)
        # 预测数据  字典转成数据框
        c = {"Glu0": fpg,
             "HbAlc": hba1c,
             "bmi": bmi,
             "age": age,
             "hr": hr,
             "ALT": alt,
             "TG": tg,
             "LDL": ldl,
             "sbp": sbp,
             "HDL": hdl
             }  # 将列表a，b转换成字典
        test = pd.DataFrame(c, index=[0])  # 将字典转换成为数据框
        test1 = ss.transform(test.values)
        test2 = pd.DataFrame(test1, columns=test.columns)
        test2 = test2[['Glu0', "HbAlc", "HDL", "age", "hr", "ALT", "TG", "LDL", "sbp", "bmi"]]
        with sess.as_default():
            with graph.as_default():
                testreslut = model2.predict(test2)
                re = round(testreslut[0, 0], 4)
                if re>=0.079:
                    return u"单纯餐后血糖升高概率:【{:.4f}】       建议进一步检测餐后血糖".format(re)
                else:
                    return u"单纯餐后血糖升高概率:【{:.4f}】 ".format(re)




if __name__ == '__main__':
    app.run_server(debug=True,dev_tools_ui=False,dev_tools_props_check=False)





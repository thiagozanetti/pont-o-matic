<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Pont'o'matic</title>
        <!-- Latest compiled and minified CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">

        <!-- Optional theme -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap-theme.min.css">

        <!-- Latest compiled and minified JavaScript -->
        <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
          <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
          <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
        <![endif]-->
    </head>
    <body>
        <div>
            <h4>Apontamentos de <strong>{{data["month"]}}</strong> para <strong>{{data["real_name"]}}</strong></h4>
        </div>
        <div class="table_responsive">
            <table class="table table-striped">
                <thead>
                    <th class="text-center">DATA</th>
                    <th class="text-center">ENTRADA</th>
                    <th class="text-center">SAÍDA PARA ALMOÇO</th>
                    <th class="text-center">RETORNO DO ALMOÇO</th>
                    <th class="text-center">SAÍDA</th>
                    <th class="text-center">HORAS TRABALHAS</th>
                    <th class="text-center">AÇÃO</th>
                </thead>
                <tbody>
                    {% for row in data["rows"]: %}
                    <tr>
                        <td class="text-center">{{row["date"]}}</td>
                        {% for appointment in row["appointments"]: %}
                        <td class="text-center">{{appointment}}</td>
                        {% endfor %}
                        <td class="text-center">09</td>
                        <td class="text-center"><input type="button" value="Criar ocorrência de ponto" /></td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    </body>
</html>
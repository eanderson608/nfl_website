<?php

  header("Access-Control-Allow-Origin: *");
  header("Content-Type: application/json; charset=UTF-8");

  echo('{
    "game1": [
            {"Day":"Mon", "Line":"-6", "Consensus": "60"},
            {"Day":"Tue", "Line":"-6", "Consensus": "59"},
            {"Day":"Wed", "Line":"-6.5", "Consensus": "55"},
            {"Day":"Thu", "Line":"-7", "Consensus": "51"}
            ],
    "game2": [
            {"Day":"Mon", "Line":"14", "Consensus": "45"},
            {"Day":"Tue", "Line":"14", "Consensus": "46"},
            {"Day":"Wed", "Line":"14.5", "Consensus": "50"},
            {"Day":"Thu", "Line":"14.5", "Consensus": "51"}
            ],
    "game3": [
            {"Day":"Mon", "Line":"-10", "Consensus": "25"},
            {"Day":"Tue", "Line":"-10.5", "Consensus": "24"},
            {"Day":"Wed", "Line":"-11", "Consensus": "25"},
            {"Day":"Thu", "Line":"-11", "Consensus": "26"}
            ]
    }');
?>

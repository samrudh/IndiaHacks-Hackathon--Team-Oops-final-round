<?php 
$ref = $ref = '';
$ref = $Comments = '';
$ref = $Comments2 = '';
$ref = $name = '';
$ref = $pro = '';
$ref = $dType = ''; 

if($name <= 10)
{
//$fun = 'inside 10';
$command = escapeshellcmd('/var/www/html/send.py');
$output = shell_exec($command);
echo $output;
}
else
{
//$fun = 'inside 11';
$command = escapeshellcmd('/var/www/html/send2.py');
$output = shell_exec($command);
}
if(isset($_GET["ref"])) $ref = $_GET["ref"]; 
if(isset($_GET["Comments"])) $Comments = $_GET["Comments"]; 
if(isset($_GET["Comments2"])) $Comments2 = $_GET["Comments2"];
if(isset($_GET["name"])) $name = $_GET["name"]; 
if(isset($_GET["pro"])) $pro = $_GET["pro"];
if(isset($_GET["dType"])) $dType = $_GET["dType"]; 

if ($ref <> ''){ 
    $fp  = fopen('commentfile.txt', 'a+'); 
    fwrite($fp, $Comments."\n");
    fwrite($fp, $ref."\n");
    fwrite($fp, $Comments2."\n");
    fwrite($fp, $name."\n");
    fwrite($fp, $pro."\n");
    fwrite($fp, $dType."\n");
   // fwrite($fp, $fun."\n");
    fclose($fp); 
} 
?>

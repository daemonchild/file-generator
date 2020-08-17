#   __ _ _                                            _
#  / _(_) | ___        __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __
# | |_| | |/ _ \_____ / _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
# |  _| | |  __/_____| (_| |  __/ | | |  __/ | | (_| | || (_) | |
# |_| |_|_|\___|      \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|
#                     |___/
#

# Powershell Client for File Generator
# Version 0.1
# Creates all possible files from API


function fetch-file ([string]$doctype, [string]$compress)
{

    $progressPreference = 'silentlyContinue'

    $URL = $APIURL + '/fetch/' + $doctype + '?compress=' + $compress
    $outfile = $doctype + '.' + $compress + '.' + $doctype

    $resp = iwr -uri $URL

    $progressPreference = 'Continue'

    return $resp.statuscode

}


function list-docs ()
{
    $URL = $APIURL + '/list/documents'
    $response = iwr -uri $URL
    $filetypes = ($response.content | ConvertFrom-Json).filetypes
    return ($filetypes)

}

function list-compress ()
{
    $URL = $APIURL + '/list/compress'
    $response = iwr -uri $URL
    $filetypes = ($response.content | ConvertFrom-Json).filetypes
    return ($filetypes)

}

function fetch-all ($docs, $compress)
{

    foreach ($d in $docs)
    {
        write-host ('- Working on: ' + $d)
        $statuscode = fetch-file -doctype $d -compress 'none'
        sleep 1
        foreach ($c in $compress)
        {
            write-host ('-- Compressing as: ' + $c)
            $statuscode = fetch-file -doctype $d -compress $c
            sleep 1

        }



    }

}



[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

$APIURL = 'http://localhost:9000'
#$PROXY = 'http://localhost:8080'

fetch-all -docs (list-docs) -compress (list-compress)

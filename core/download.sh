# NOT USED here for reference

#!/bin/bash

# Script for downloading audio clips (10s) from Youtube using AudioSet CSV datasets

# SAMPLE_RATE=22050

# # fetch_clip(videoID, startTime, endTime)
# fetch_clip() {
#   echo "Fetching $1 ($2 to $3)..."
#   outname="$1_$2"
#   if [ -f "${outname}.wav.gz" ]; then
#     echo "Already have it."
#     return
#   fi

#   if [ $? -eq 0 ]; then
#     # i.e. if we haven't found this file
#     ffmpeg -loglevel quiet -ss "$2" -t 10 \
#         -i $(youtube-dl -f 'bestaudio' --get-url https://youtube.com/watch?v=$1) \
#         -ar $SAMPLE_RATE \
#         "./$outname.wav"
#    else
#     sleep 1
#    fi
# }

# # iterate through the input piped into script
# grep -E '^[^#]' | while read line
# do
#   fetch_clip $(echo "$line" | sed -E 's/,/ /g')
# done

@echo off
setlocal enabledelayedexpansion

REM Script for downloading audio clips (10s) from Youtube using AudioSet CSV datasets

set SAMPLE_RATE=22050

REM fetch_clip(videoID, startTime, endTime)
:fetch_clip
echo Fetching %1 (%2 to %3)...
set outname=%1_%2
if exist "!outname!.wav.gz" (
    echo Already have it.
) else (
    youtube-dl -f bestaudio --get-url https://youtube.com/watch?v=%1 > tmp_url.txt
    set /p yt_url=<tmp_url.txt
    ffmpeg -loglevel quiet -ss %2 -t 10 -i !yt_url! -ar %SAMPLE_RATE% ".\!outname!.wav"
    del tmp_url.txt
)
goto :eof

REM iterate through the input piped into script
for /f "delims=" %%a in ('findstr /r /v "^#"') do (
    call :fetch_clip %%a
)

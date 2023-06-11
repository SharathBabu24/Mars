#!/bin/bash

# Taking the number of charecters as the input parameter
length="$1"

# Setting the characters that can be used in the password
characters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+{}[]|;:,.<>?/~\`"

# Generate the random password
password=$(cat /dev/urandom | tr -dc "$characters" | fold -w "$length" | head -n 1)

echo "Random password generated using /dev/urandom:"
echo "$password"


# Generate the random password using pwgen
password=$(pwgen -s -1 "$length")

echo "Random password generated using pwgen:"
echo "$password"

<script>
    let count = 0;

    function clicked() {
        count += 1;

        document.getElementById("clicks").innerText =
            "Pressed " + count + " times";
    }
</script>

<button class="btn btn-secondary btn-block" id="clicks" onclick="clicked()">
    Pressed 0 times
</button>

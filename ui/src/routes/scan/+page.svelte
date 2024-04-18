<script>
	import Quagga from 'quagga';
	import { onMount } from 'svelte';

	onMount(() => {
		Quagga.init(
			{
				inputStream: {
					name: 'Live',
					type: 'LiveStream',
					target: document.getElementById("scan")
				},
				decoder: {
					readers: ['code_128_reader']
				}
			},
			function (/** @type {any} */ err) {
				if (err) {
					console.log(err);
					return;
				}
				console.log('Initialization finished. Ready to start');
				Quagga.start();
			}
		);
        Quagga.onDetected((/** @type {any} */ data) => {
            const barcode = data.codeResult.code;
            console.log(barcode);
            Quagga.stop();
            // TODO (1) get info on the scanned barcode via some API or my backend with spinning wheel (2) route to products/[id]
        })
	});
</script>

Let's scan
<div id="scan"></div>
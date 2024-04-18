<script>
	import { page } from '$app/stores';
	export const data = [
		{
			vitae: 'dolorem',
			lectus: 'ipsum',
			quisquam: 'quia'
		},
		{
			vitae: 'amet',
			lectus: 'consectetur',
			quisquam: 'adipisci'
		}
	];
</script>

Slug in URL: {$page.params.slug}

<table>
	<thead>
		<tr>
			{#each Object.keys(data[0]) as columnTitle}
				<th>{columnTitle}</th>
			{/each}
		</tr>
	</thead>
	<tbody>
		{#each Object.values(data) as row}
			<tr>
				{#each Object.values(row) as cell}
					<td>{cell}</td>
				{/each}
			</tr>
		{/each}
	</tbody>
</table>

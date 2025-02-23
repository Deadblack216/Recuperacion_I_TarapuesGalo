# first line: 1
@memory.cache
def load_20newsgroups() -> Tuple[List[str], List[str], List[int]]:
    dataset = fetch_20newsgroups(
        subset='all',
        remove=('headers', 'footers', 'quotes'),
        shuffle=True,
        random_state=42
    )
    return dataset.data, dataset.target_names, dataset.target

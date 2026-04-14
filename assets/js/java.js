function toggleCase(btn) {
    const currentItem = btn.closest('.case-item');
    const isOpen = currentItem.classList.contains('open');

    // Close all other open items
    document.querySelectorAll('.case-item.open').forEach(item => {
        item.classList.remove('open');
    });

    // If the clicked item wasn't open, open it
    if (!isOpen) {
        currentItem.classList.add('open');
    }
}
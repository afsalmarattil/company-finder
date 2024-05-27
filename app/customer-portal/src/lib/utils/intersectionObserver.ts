export const intersectionObserver = (node: Element, callback: () => void) =>{
    const observer = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting) {
            callback();
        }
    }, {
        root: null,
        rootMargin: '0px',
        threshold: 1.0
    });

    observer.observe(node);

    return {
        destroy() {
            observer.unobserve(node);
        }
    };
}

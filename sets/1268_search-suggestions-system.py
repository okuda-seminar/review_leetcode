'''
Q[1268]. Search Suggestions System
'''

# n = len(products)
# m = len(searchWord)
# time : max(O(nlogn), O(m * n))
# space : O(n)


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        '''Return suggests at most three product names from products
        Args:
            products(List[str]):the array consist of strings (1 <= len(products) <= 1000)
            searchWord(str): a string (1 <= len(searchWord) <= 1000)
        Returns:
            List[List[str]]: suggests at most three product names from products
        '''
        if not products:
            raise ValueError('products length should be [1, 1000]')

        if not searchWord:
            raise ValueError('searchWord length should be [1, 1000]')

        SUGGEST_NUM = 3
        suggest_products = []
        products.sort()

        for i in range(len(searchWord)):
            cur_suggest_products = []

            for product in products:
                if len(cur_suggest_products) == SUGGEST_NUM:
                    break

                if product[:i+1] == searchWord[:i+1]:
                    cur_suggest_products.append(product)

            suggest_products.append(cur_suggest_products)
        return suggest_products


# time : max(O(nlogn), O(m * n))
# space : O(n)


import heapq


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        SUGGEST_NUM = 3
        suggest_products = []
        sorted_products = []

        for product in products:
            heapq.heappush(sorted_products, product)

        for i, char in enumerate(searchWord):
            if not sorted_products:
                suggest_products.append([])
                continue

            buffer = []
            while sorted_products and len(buffer) < SUGGEST_NUM:
                cur_product = heapq.heappop(sorted_products)
                if len(cur_product) >= i + 1 and cur_product[:i+1] == searchWord[:i+1]:
                    buffer.append(cur_product)

            for product in buffer:
                heapq.heappush(sorted_products, product)

            suggest_products.append(buffer)

        return suggest_products

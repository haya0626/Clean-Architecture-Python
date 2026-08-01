# ABC：抽象クラスの親クラス
# abstractmethod：継承先で実装必須にするためのデコレーター
class ProductRepository(ABC):

    @abstractmethod
    async def search(
        self,
        product_name: str | None,
    ) -> list[Product]:

        raise NotImplementedError
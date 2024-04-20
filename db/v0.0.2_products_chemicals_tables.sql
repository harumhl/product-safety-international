CREATE TABLE products (
    id uuid NOT NULL PRIMARY KEY,
    barcode text
);

CREATE TABLE chemicals (
    id uuid NOT NULL PRIMARY KEY
);

CREATE TABLE productsChemicals (
    productId uuid NOT NULL references products(id),
    chemicalId uuid NOT NULL references chemicals(id)
);

CREATE TABLE productTranslations (
    id uuid NOT NULL references products(id),
    language text NOT NULL,
    isDefault boolean NOT NULL,
    name text NOT NULL
);

CREATE TABLE chemicalTranslations (
    id uuid NOT NULL references chemicals(id),
    language text NOT NULL,
    isDefault boolean NOT NULL,
    score int
);

CREATE TABLE chemicalDetails (
    id uuid NOT NULL references chemicals(id),
    details text,
    source text
);
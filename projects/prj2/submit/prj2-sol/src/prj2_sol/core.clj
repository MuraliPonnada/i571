(ns prj2-sol.core)

(defrecord OrderItem
  [ sku        ;keyword ID identifying item
    category   ;keyword giving item category
    n-units    ;# of units of item
    unit-price ;price per unit of item
  ])

;; #1: 15-points
;;given a list items of OrderItem, return the total for
;;the order, i.e. sum n-units*unit-price over all items
;;must be recursive but cannot use loop or recur
(defn items-total1 [items]
  "return total price of all items"
  (cond (empty? items)
        0
        :else
        (+ (* (:n-units (first items)) (:unit-price (first items)))
           (items-total1 (rest items)))))

;; #2: 15-points
;;given a list items of OrderItem and a category,
;;return list of elements of items having specified category.
;;must be implemented using recursion
(defn items-with-category1 [items category]
  "return sublist of items having specified category"
  (if (empty? items)
    '()
    (let [item (first items)
          rest-items (rest items)]
      (if (= category (:category item))
        (cons item (items-with-category1 rest-items category))
        (items-with-category1 rest-items category)))))

;; #3: 15-points
;;same specs as items-total1 but must be implemented using
;;loop and recur
(defn items-total2 [items]
  "return total price of all items"
  (loop [total 0
         remaining-items items]
    (if (empty? remaining-items)
      total
      (let [item (first remaining-items)
            rest-items (rest remaining-items)]
        (recur (+ total (* (:n-units item) (:unit-price item)))
               rest-items)))))

;; #4: 10-points
;;given a list items of OrderItem return a list of all the :sku's
;;cannot use explicit recursion
(defn item-skus [items]
  "return :sku's of all items"
  (reduce #(conj %1 (:sku %2)) [] items))

;; #5: 10-points
;;given a list items of OrderItem, return a list of skus of those elements
;;in items having unit-price greater than price
;;cannot use explicit recursion
(defn expensive-item-skus [items price]
  "return list of :sku's of all items having :unit-price > price"
  (letfn [(filter-expensive [item] (> (:unit-price item) price))]
    (->> items
         (filter filter-expensive)
         (map #(:sku %))
         (into []))))

;; #6: 10-points
;;same specs as items-total1 but cannot use explicit recursion
(defn items-total3 [items]
  "return total price of all items" 
  (let [sum-of-prices (fn [total item] (+ total (* (:n-units item) (:unit-price item))))]
    (reduce sum-of-prices 0 items)))
  

;; #7: 10-points
;;same spec as items-with-category1, but cannot use explicit recursion
(defn items-with-category2 [items category]
  "return sublist of items having specified category"
  (filter #(= (:category %) category) items))

;; #8: 15-points 
;;given a list items of OrderItem and an optional category
;;return total of n-units of category in items.  If the
;;optional category is not specified, return total of n-units
;;of all items.
;;cannot use explicit recursion
(defn item-category-n-units 
  "return sum of :n-units of items for category (all categories if unspecified)"
  ([items] 
  (item-category-n-units items nil))
  ([items category] 
  (let [filtered-items (if category
                           (items-with-category2 items category)
                           items)]
     (reduce + (map :n-units filtered-items)))))

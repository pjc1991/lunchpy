import lunchpy.slack.slack_util as slack_util
import lunchpy.recommend.recommend as recommend
import lunchpy.config as config
import lunchpy.stores.store_collector as store_collector


if __name__ =='__main__':
    matzips = store_collector.get_matzips_from_naver()
    # print the number of stores
    print(f"the number of stores {len(matzips)}")
    # print all 
    for matzip in matzips:
        # name rating address
        print(matzip.name, matzip.rating, matzip.address)